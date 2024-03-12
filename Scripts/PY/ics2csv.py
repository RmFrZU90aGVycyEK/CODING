import csv
import datetime
import icalendar

def ICSToCSV(ics_file, csv_file):
    with open(ics_file, 'rb') as f:
        cal = icalendar.Calendar.from_ical(f.read())

    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Event', 'Start', 'End', 'Description'])
        for component in cal.walk():
            if component.name == 'VEVENT':
                summary = component.get('summary')
                start = component.get('dtstart').dt
                end = component.get('dtend').dt
                description = component.get('description')
                writer.writerow([summary, start, end, description])

ICSToCSV('./calendar.ics', './icalendar.csv')
