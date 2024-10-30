from framework.app import App
from controllers.calendar_controller import CalendarController

app = App()
calendar_controller = CalendarController()

@app.route("/")
def home():
    return "Welcome to the Calendar App!"

@app.route("/events")
def show_events():
    # Show events using the PyQt graphical interface
    calendar_controller.show_events()
    return "Events displayed in GUI."

if __name__ == "__main__":
    # Add sample events for testing
    calendar_controller.add_event("Meeting", "2024-11-10", "Project meeting at 10 AM")
    calendar_controller.add_event("Workshop", "2024-11-15", "Python workshop")
    calendar_controller.show_events()
    app.start()
