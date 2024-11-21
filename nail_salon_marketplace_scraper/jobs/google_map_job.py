from nail_salon_marketplace_scraper.app import app, db
from nail_salon_marketplace_scraper.service.google_maps_service import get_places, get_place_details
from nail_salon_marketplace_scraper.models import NailSalon

# TODO: Evolve this to be more dynamic
text_queries = ["nail salon in new york city"]


def populate_nail_salons():
    """
    Fetch places and populate the nail_salons database table.
    """
    # Store all place IDs from the queries
    places_ids = []
    for query in text_queries:
        places = get_places(query)  # Call your service to fetch places
        places_ids.extend(places)

    # Iterate over place IDs to fetch details and populate the database
    for place_id in places_ids:
        place_info = get_place_details(place_id)
        name = place_info.get("displayName").get("text")
        #cur_hours = str(place_info.get("currentOpeningHours"))
        website = place_info.get("websiteUri")
        address = place_info.get("formattedAddress")
        maps_uri = place_info.get("googleMapsUri")
        phone = place_info.get("nationalPhoneNumber")
        place_id = place_info.get("id")

        # Check for duplicates before adding to the database
        if not db.session.query(NailSalon).filter_by(place_id=place_id).first():
            new_salon = NailSalon(
                place_id=place_id,
                display_name=name,
                formatted_address=address,
                national_phone_number=phone,
                website_uri=website,
                google_maps_uri=maps_uri,
            )
            db.session.add(new_salon)

    # Commit the changes
    db.session.commit()
    print(f"Populated {len(places_ids)} new nail salons into the database.")


# Schedule the job to run daily using Flask-APScheduler
@app.scheduler.task('interval', id='populate_nail_salons', minutes=1)
def scheduled_job():
    """
    Scheduled job to run the populate_nail_salons function daily.
    """
    print("Running scheduled job to populate nail salons...")
    populate_nail_salons()
