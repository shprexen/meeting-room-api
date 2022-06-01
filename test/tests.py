from src.db import SessionLocal


def test_organization_rooms_endpoint(test_app, organization, db_rooms):
    with SessionLocal.begin() as session:
        session.add(organization)
        response = test_app.get(f"/organizations/{organization.id}/rooms/")

    db_rooms = sorted([room.dict() for room in db_rooms], key=lambda x: x["id"])

    assert response.status_code == 200
    assert response.json() == db_rooms


def test_create_room(test_app, room_number, organization):
    with SessionLocal.begin() as session:
        session.add(organization)
        successfull_response = test_app.post(
            f"/organizations/{organization.id}/rooms/",
            json={"room_number": room_number},
        )
        error_response = test_app.post(
            f"/organizations/{organization.id}/rooms/",
            json={"room_number": room_number},
        )
    assert successfull_response.status_code == 201
    assert error_response.status_code == 400


def test_delete_room(test_app, db_rooms):
    room_id = db_rooms[0].id
    successfull_response = test_app.delete(
        f"/rooms?room_id={room_id}",
    )
    assert successfull_response.status_code == 204
    error_response = test_app.delete(
        f"/rooms?room_id={room_id}",
    )
    assert error_response.status_code == 400
