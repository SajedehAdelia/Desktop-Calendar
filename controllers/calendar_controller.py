from models.calendar_event import CalendarEvent
from views.calendar_view import run_calendar_view

class CalendarController:
    def __init__(self):
        self.events = []

    def add_event(self, title, date, description=""):
        event = CalendarEvent(title, date, description)
        self.events.append(event)

    def remove_event(self, title):
        self.events = [event for event in self.events if event.title != title]

    def show_events(self):
        run_calendar_view(self.events)
