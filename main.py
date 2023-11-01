import pandas
import pm4py


def run_analyzer():
    event_log_raw = pandas.read_csv("data/git_event_matrix_05_file_name_included_as_activity.csv")
    event_log_raw["case:concept:name"] = event_log_raw["repository_owner"] + event_log_raw["repository_name"]      # case id
    event_log_raw["concept:name"] = event_log_raw["event_type"] + event_log_raw["action"]                           # activity
    event_log_raw["time:timestamp"] = pandas.to_datetime(event_log_raw["action_time"])                              # timestamp
    
    event_log = event_log_raw[event_log_raw['case:concept:name'].str.len() > 0]
    
    
    dfg, start_activities, end_activities = pm4py.discover_dfg(event_log)
    pm4py.view_dfg(dfg, start_activities, end_activities, format='jpg')
    tree = pm4py.discover_process_tree_inductive(event_log)
    pm4py.view_process_tree(tree, format='jpg')
    net, initial_marking, final_marking = pm4py.convert_to_petri_net(tree)
    pm4py.view_petri_net(net, initial_marking, final_marking, format='jpg')
    bpmn = pm4py.convert_to_bpmn(net, initial_marking, final_marking)
    pm4py.view_bpmn(bpmn, format='jpg')
    
    """
    process_tree = pm4py.discover_process_tree_inductive(event_log)
    pm4py.view_process_tree(process_tree)
    """


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_analyzer()
