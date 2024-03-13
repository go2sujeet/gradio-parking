import time
from data_classes import Event, TimeWindow
import datetime
import json

def twenty_four_hours_bucket_time_series_by_minute(valid_events:list[Event],target_date:datetime)->(list[int],list[list[Event]]): # type: ignore
    #create a pre defined time window for 24 hours by minute precision
    twenty_four_hour_by_minutes_array = [0]*(24*60)
    twenty_four_hour_by_minutes_events_array = [[]]*(24*60)
    default_start_time = 0
    default_end_time = 24*60
    for event in valid_events:
        if(event.entrance_time.date() != target_date.date()):
            start_time:time = default_start_time
        else:
            start_time:time = event.entrance_time.time().hour*60 + event.entrance_time.time().minute
        if(event.exit_time.date() != target_date.date()):
            end_time:time = default_end_time
        else:
            end_time:time = event.exit_time.time().hour*60 + event.exit_time.time().minute
            
        for i in range(start_time,end_time):
            twenty_four_hour_by_minutes_array[i] += 1
            twenty_four_hour_by_minutes_events_array[i].append(event)

    return (twenty_four_hour_by_minutes_array,twenty_four_hour_by_minutes_events_array)

def find_max_continuous_sequence(x):
    # Find the maximum continuous sequence of the maximum element
    max_element = max(x)
    # Find the maximum continuous sequence of the maximum element
    start = -1
    end = -1
    current_start = -1
    current_length = 0
    max_length = 0

    for i in range(len(x)):
        if x[i] == max_element:
            if current_start == -1:
                current_start = i
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
                start = current_start
                end = i - 1
            current_start = -1
            current_length = 0

    # Check if the last sequence is the maximum continuous sequence
    if current_length > max_length:
        start = current_start
        end = len(x) - 1

    return (max_element, start, end)

def loadDataFromJson():
    with open('data/events.json') as f:
        data = json.load(f)
    return data

def filter_event_by_date_facility_id(event:Event,target_date:datetime, facility_id:int):
    if event.facility_id == facility_id: 
        if event.entrance_time.date() <= target_date.date() and event.exit_time.date() >= target_date.date():
            return True
    else:
        return False