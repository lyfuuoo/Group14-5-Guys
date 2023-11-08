from backend.models.event_info_model import EventInfoModel, ClubInfoModel # noqa
from models.event_info_model_mock_data import event_info_model_mock_data
from models.event_filter_model import EventFilerModel
from models.event_filter_model_mock_data import filter_info_model_mock_data
from models.club_info_model_mock_data_2 import club_info_mock_data


def event_info_mocking(db):
    mock_data_models = event_info_model_mock_data
    for mock_data in mock_data_models:
        print(mock_data["club_id"])
        event_info_instance = EventInfoModel(
            event_name=mock_data["event_name"],
            event_time=mock_data["event_time"],
            number_rater=mock_data["number_rater"],
            average_rating=mock_data["average_rating"],
            event_description=mock_data["event_description"],
            event_image=mock_data["event_image"],
            club_id=mock_data["club_id"]
        )
        print(event_info_instance)
        db.session.add(event_info_instance)
        db.session.commit()


def filter_info_mocking(db):
    mock_filters = filter_info_model_mock_data
    print(mock_filters)
    for mock_filter in mock_filters:
        filter_instance = EventFilerModel(
            mock_filter["event_id"],
            mock_filter["filter"]
        )
        print(filter_instance)
        db.session.add(filter_instance)
        db.session.commit()


def club_info_mocking(db):
    mock_club = club_info_mock_data
    for md in mock_club:
        club_instance = ClubInfoModel(
            md["club_name"],
            md["host_name"],
            md["description"]
        )
        print(club_instance)
        db.session.add(club_instance)
        db.session.commit()
