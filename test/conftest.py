import random
import string

import pytest
from starlette.testclient import TestClient

from src.schemas import MeetingRoom as MeetingRoomSchema
from src.models import Organization, MeetingRoom
from src.app import app
from src.db import SessionLocal


def __random_string(char_num: int) -> str:
    return "".join(random.choice(string.ascii_letters) for _ in range(char_num))


@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client


@pytest.fixture()
def room_number():
    return __random_string(8)


@pytest.fixture()
def organization():
    org = Organization(
        id=random.randint(1, 1000), organization_name=__random_string(10)
    )

    with SessionLocal.begin() as session:
        session.add(org)
    yield org

    with SessionLocal.begin() as session:
        session.delete(org)


@pytest.fixture()
def db_rooms(organization):
    db_rooms = []
    serialized_rooms = []
    with SessionLocal.begin() as session:
        session.add(organization)

        for _ in range(5):
            room = MeetingRoom(
                id=random.randint(500, 1000),
                room_number=__random_string(6),
                organization_id=organization.id,
            )
            db_rooms.append(room)
            serialized_rooms.append(MeetingRoomSchema.from_orm(room))

        session.add_all(db_rooms)

    yield serialized_rooms

    with SessionLocal.begin() as session:
        session.query(MeetingRoom).delete()
