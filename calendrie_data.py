from ics import Calendar
import os

def get_calendar_events():
    calendar_file = os.path.expanduser('~/.local/share/evolution/calendar/system/calendar.ics')  # Chemin vers le fichier de calendrier GNOME

    with open(calendar_file, 'r') as f:
        c = Calendar(f.read())

    events = []

    for event in c.events:
        event_dict = {
            "summary": event.name,
            "start": event.begin.strftime('%Y-%m-%d %H:%M:%S'),
            "end": event.end.strftime('%Y-%m-%d %H:%M:%S'),
            "description": event.description,
        }
        events.append(event_dict)

    return events

if __name__ == "__main__":
    events = get_calendar_events()

    # Afficher les événements
    for event in events:
        print(event)
