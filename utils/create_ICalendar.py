from datetime import datetime, timedelta
from icalendar import Calendar, Event
import pytz

# Set timezone (adjust if needed)
tz = pytz.timezone('America/New_York')

duration = {
  "lollipop": 4 * 8,
  "wing": 4 * 10,
  "striker": 4 * 15,
}


def create_ICalendar(collections):
  # Create calendar
  cal = Calendar()
  cal.add('prodid', '-//Youth Soccer Schedule//mxm.dk//')
  cal.add('version', '2.0')

  print(collections)
  for game in collections:

    date_str, time_str, field_location, field_number, home_coach, visitor_coach, division, player = game


    # Combine date and time
    dt_start = tz.localize(datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %I:%M %p"))
    dt_end = dt_start + timedelta(minutes=duration[division])

    # Create event
    event = Event()
    event.add('summary', f" {player} Soccer Game ({division})")
    event.add('dtstart', dt_start)
    event.add('dtend', dt_end)
    event.add('location', f"{field_location} - Field #{field_number}")
    event.add('description', f"Division: {division}\nField: {field_location} #{field_number}")
    event.add('dtstamp', datetime.now(tz))

    cal.add_component(event)

    # Write to .ics file
  with open("./data/2025_soccer_schedule.ics", "wb") as f:
    f.write(cal.to_ical())

  print("✅ iCalendar file 'soccer_schedule.ics' created.")
