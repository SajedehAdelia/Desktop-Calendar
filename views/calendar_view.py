from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QLabel, addWidget
import sys

class CalendarView(QWidget):
    def __init__(slef, events):
        super().__init__()
        self.events = events
        self.init_ui() 

    def init_ui(self):
        #The main layout
        self.setWindowTitle("Calendar Events")
        layout = QVBoxLayout()

        #Title label
        title = QLabel(" Upcoming events ! ")
        layout.addWidget(title)

        # List widget to display list 
        self.event_list = QListWidget()
        self.update_event_list()
        layout.addWidget(self.event_list)

        self.setLayout(layout)

    def update_event_list(self):
        # Update and populate the list with new data
        self.event_list.clear()
        for event in self.events:
            self.event_list.addItem(f"{event.title} on {event.date}: {event.description}")

    def show_events(self):
        # Display the window
        self.show()


def run_calendar_view(events):
    app = QApplication(sys.argv)
    view = CalendarView(events)
    view.show_events()
    sys.exit(app.exec_())
