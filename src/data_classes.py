from ast import Dict, List
from dataclasses import dataclass
import datetime

future_exit_time = datetime.datetime(9999, 12, 31, 23, 59, 59)
@dataclass
class Event:
    id: int
    trailer_id: int
    facility_id: int
    entrance_time: datetime
    exit_time: datetime
    @classmethod
    def from_dict(cls, data: Dict):
        return cls(
            id=data["id"],
            trailer_id=data["trailer_id"],
            facility_id =data["facility_id"],
            entrance_time = datetime.fromisoformat(data["entrance_time"]),
            exit_time = (datetime.fromisoformat(data["exit_time"]) if data["exit_time"] != None else future_exit_time),
        )


from dataclasses import dataclass, field
from typing import List
from datetime import datetime

@dataclass
class TimeWindow:
    start_time: datetime
    exit_time: datetime
    events: List[Event] = field(default_factory=list)

    @classmethod
    def from_event(cls, event: Event):
        return cls(
            start_time=event.entrance_time,
            exit_time=event.exit_time,
            events=[event]
        )

    def get_events_count(self):
        return len(self.events)
    
    def has_overlap_with_event(self, event: Event):
        # when the event overlaps with the window from the left
        if event.exit_time >=self.start_time and event.entrance_time <=self.start_time:
            return True
        # when the event overlaps with the window from the right
        elif event.entrance_time <=self.exit_time and event.exit_time >=self.exit_time:
            return True
        # when the event is completely inside the window
        elif event.entrance_time >=self.start_time and event.exit_time <=self.exit_time:
            return True
        else:
            return False
        
    def is_exact_match(self, event: Event):
        return event.entrance_time == self.start_time and event.exit_time == self.exit_time
