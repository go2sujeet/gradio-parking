from datetime import datetime
import json
from data_classes import Event, TimeWindow
from utils import filter_event_by_date_facility_id, find_max_continuous_sequence, get_all_facility_ids, loadDataFromJson, twenty_four_hours_bucket_time_series_by_minute
import gradio as gr
from gradio_calendar import Calendar

def find_most_occupied_window(target_date:datetime, target_facility_id:int):
    data = loadDataFromJson()
    valid_events = [Event.from_dict(event) for event in data if filter_event_by_date_facility_id(Event.from_dict(event), target_date, target_facility_id)]
    occupied_spots_per_minute,max_occupied_spots_by_events_by_minutes = twenty_four_hours_bucket_time_series_by_minute(valid_events,target_date)
    _max,start_time, end_time = find_max_continuous_sequence(occupied_spots_per_minute)
    #convert start and end time to datetime
    start_time = datetime(target_date.year, target_date.month, target_date.day, start_time//60, start_time%60)
    end_time = datetime(target_date.year, target_date.month, target_date.day, end_time//60, end_time%60)
    max_sequence = (start_time.__str__(), end_time.__str__())
    return ([start_time, end_time],max(occupied_spots_per_minute), occupied_spots_per_minute)

target_date = datetime.fromisoformat("2022-01-18 00:00:00")
target_facility_id = 1
result = find_most_occupied_window(target_date, target_facility_id) 
#problem 1
print("Most number of slots at the same time is {}".format(result[1]))
#problem 2
print("Most occupied window is between {} and {} with {} occupied spots".format(result[0][0],result[0][1],result[1]))

def process1(target_date, target_facility_id):
    result = find_most_occupied_window(target_date, target_facility_id) 
    return "Most occupied window is between {} and {} with {} occupied spots".format(result[0][0],result[0][1],result[1])

all_facility_ids = get_all_facility_ids()
with gr.Blocks() as app:
    with gr.Group():
        target_date = Calendar(label="Target Date",value=target_date)
        target_facility_id = gr.Dropdown(label="Facility ID",choices=all_facility_ids,value=all_facility_ids[0])
        btn_1 = gr.Button(value="Find Most Occupied Window")
    output1 = gr.Text(label="Most Occupied Window",show_copy_button = True)
    btn_1.click(process1, [target_date, target_facility_id], outputs=output1)


if __name__ == "__main__":
    app.launch()