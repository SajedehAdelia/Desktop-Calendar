cclass CalendarEvent:
    def __init__(self, title, date, description=""):
        self.title = title        # Title of the event
        self.date = date          # Date of the event (ideally in YYYY-MM-DD format)
        self.description = description  # Optional description for more details

    def update_event(self, title=None, date=None, description=None):
        """Updates the event's details if new data is provided."""
        if title:
            self.title = title
        if date:
            self.date = date
        if description:
            self.description = description

    def get_details(self):
        """Returns a string representation of the event's details."""
        return f"{self.title} on {self.date}: {self.description}"

    def __repr__(self):
        return self.get_details()
