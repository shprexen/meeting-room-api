from typing import List

from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session
from starlette import status

from src import schemas
from src.db import get_session
import src.services.room_service as crud


router = APIRouter()


@router.post(
    "/organizations/{org_id}/rooms/",
    response_model=schemas.MeetingRoom,
    status_code=status.HTTP_201_CREATED,
)
def create_room_for_organization(
    org_id: int,
    room: schemas.MeetingRoomCreate,
    session: Session = Depends(get_session),
):
    return crud.create_room(session=session, org_id=org_id, room=room)


@router.get(
    "/organizations/{org_id}/rooms/",
    response_model=List[schemas.MeetingRoom],
    status_code=status.HTTP_200_OK,
)
def get_organization_rooms(org_id: int, session: Session = Depends(get_session)):
    org_rooms = crud.get_organization_rooms(session=session, org_id=org_id)
    return org_rooms


@router.delete(
    "/rooms", status_code=status.HTTP_204_NO_CONTENT, response_class=Response
)
def delete_room(room_id: int, session: Session = Depends(get_session)):
    crud.delete_room(session=session, room_id=room_id)
