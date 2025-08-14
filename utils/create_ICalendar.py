from datetime import datetime, timedelta
from icalendar import Calendar, Event
import pytz
from dataclasses import field
from data.targetTeams import gameLocation



# Set timezone (adjust if needed)
tz = pytz.timezone('America/New_York')

duration = {
  "lollipop": 4 * 8,
  "wing": 4 * 10,
  "striker": 4 * 15,
}


def format_location (location):
  parse_out_number = ''.join([i for i in location if not i.isdigit()])
  print(parse_out_number)
  # if parse_out_number:
  #   return location[parse_out_number]

  # return gameLocation['default']

   # return f"{playing_location.address}, {playing_location.city}, {playing_location.state}, {playing_location.zip_code}"


def create_ICalendar(collections):
  # Create calendar
  cal = Calendar()
  cal.add('prodid', '-//Youth Soccer Schedule//mxm.dk//')
  cal.add('version', '2.0')

  for game in collections:

    date_str, time_str, field_location, field_number, home_coach, visitor_coach, division, player = game


    # Combine date and time
    dt_start = tz.localize(datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %I:%M %p"))
    dt_end = dt_start + timedelta(minutes=duration[division])

    playing_field = field_number if field_number == 'N/A' else field_location
    playing_location =  format_location(field_location)


    # print(playing_location)


    # Create event
    event = Event()
    event.add('summary', f" {player} Soccer Game ({division})")
    event.add('dtstart', dt_start)
    event.add('dtend', dt_end)
    event.add('location',playing_location )
    event.add('description', f"Field: # {playing_field}")
    event.add('dtstamp', datetime.now(tz))

    cal.add_component(event)

    # Write to .ics file
  # with open("./data/2025_soccer_schedule.ics", "wb") as f:
  #   f.write(cal.to_ical())

  print("✅ iCalendar file 'soccer_schedule.ics' created.")
