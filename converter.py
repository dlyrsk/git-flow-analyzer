import pandas
import pm4py


def convert_csv_to_xes_repo_as_case(name):
    event_log_raw = pandas.read_csv(f"data/{name}.csv")
    event_log_raw["case:concept:name"] = event_log_raw["repository_owner"] + '/' + event_log_raw["repository_name"]
    event_log_raw["concept:name"] = event_log_raw["event_type"] + event_log_raw["action"]  # activity
    event_log_raw["time:timestamp"] = pandas.to_datetime(event_log_raw["action_time"])  # timestamp
    event_log_raw["org:resource"] = event_log_raw["actor_name"]     # resource
    
    event_log_raw = event_log_raw.sort_values(by='time:timestamp')
    
    pm4py.write_xes(event_log_raw, f"data/{name}_repo_as_case.xes")


def convert_csv_to_xes_actor_as_case(name):
    event_log_raw = pandas.read_csv(f"data/{name}.csv")
    event_log_raw["case:concept:name"] = event_log_raw["actor_id"] + '-' + event_log_raw["actor_name"]
    event_log_raw["concept:name"] = event_log_raw["event_type"] + event_log_raw["action"]  # activity
    event_log_raw["time:timestamp"] = pandas.to_datetime(event_log_raw["action_time"])  # timestamp
    event_log_raw["org:resource"] = event_log_raw["actor_name"]     # resource
    
    event_log_raw = event_log_raw.sort_values(by='time:timestamp')
    
    pm4py.write_xes(event_log_raw, f"data/{name}_actor_as_case.xes")
    

def convert_csv_to_xes_file_as_case(name):
    event_log_raw = pandas.read_csv(f"data/{name}.csv")
    event_log_raw["case:concept:name"] = event_log_raw["filename"]
    event_log_raw["concept:name"] = event_log_raw["event_type"] + event_log_raw["action"]  # activity
    event_log_raw["time:timestamp"] = pandas.to_datetime(event_log_raw["action_time"])  # timestamp
    event_log_raw["org:resource"] = event_log_raw["actor_name"]  # resource
    
    event_log_raw = event_log_raw.sort_values(by='time:timestamp')
    event_log_raw = event_log_raw[event_log_raw['case:concept:name'].str.len() > 0]
    
    pm4py.write_xes(event_log_raw, f"data/{name}_file_as_case.xes")


if __name__ == '__main__':
    name = "git_event_sydent_01"
    #convert_csv_to_xes_repo_as_case(name)
    #convert_csv_to_xes_actor_as_case(name)
    convert_csv_to_xes_file_as_case(name)
