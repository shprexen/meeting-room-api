from typing import List

from pydantic import BaseModel


class MeetingRoom(BaseModel):
    id: int
    room_number: str
    organization_id: int

    class Config:
        orm_mode = True


class MeetingRoomCreate(BaseModel):
    room_number: str

    class Config:
        orm_mode = True


class MeetingRoomDelete(BaseModel):
    id: int

    class Config:
        orm_mode = True


class Organization(BaseModel):
    id: int
    organization_name: str
    rooms: List[MeetingRoom] = []

    class Config:
        orm_mode = True
