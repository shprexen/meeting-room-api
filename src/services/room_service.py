from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette import status

import src.models as models
import src.schemas as schemas
from src.custom_logging import logger


def get_organization(session: Session, org_id: int):
    return (
        session.query(models.Organization)
        .filter(models.Organization.id == org_id)
        .first()
    )


def get_rooms(session: Session, skip: int = 0, limit: int = 100):
    return session.query(models.MeetingRoom).offset(skip).limit(limit).all()


def get_organization_rooms(session: Session, org_id: int):
    organization = get_organization(session=session, org_id=org_id)
    if organization is None:
        logger.info(f"Organization with id={org_id} doesn't exist")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="There isn't such organization",
        )

    logger.info(f"{organization.organization_name}'s rooms has been requested")
    return (
        session.query(models.MeetingRoom)
        .filter(models.MeetingRoom.organization_id == org_id)
        .all()
    )


def create_room(session: Session, room: schemas.MeetingRoomCreate, org_id: int):
    if room_exists(session=session, room=room):
        logger.info(f"Room with number={room.room_number} already exists")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Such room has already been created",
        )

    db_room = models.MeetingRoom(organization_id=org_id, room_number=room.room_number)
    session.add(db_room)
    session.commit()
    session.refresh(db_room)

    logger.info(f"{db_room.room_number} has been created successfully")
    return db_room


def delete_room(session: Session, room_id: int):
    room = (
        session.query(models.MeetingRoom)
        .filter(models.MeetingRoom.id == room_id)
        .first()
    )
    if room is None:
        logger.info(f"Meeting room with id={room_id} doesn't exist")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="There isn't such room"
        )

    session.delete(room)
    session.commit()

    logger.info(f"{room.room_number} has been deleted successfully")


def room_exists(session: Session, room: schemas.MeetingRoomCreate):
    exists = session.query(
        session.query(models.MeetingRoom)
        .filter(models.MeetingRoom.room_number == room.room_number)
        .exists()
    ).scalar()
    return exists
