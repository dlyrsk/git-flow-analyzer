import pm4py


def run_analyzer():
    dfg, start_activities, end_activities = pm4py.discover_dfg(log)
    pm4py.view_dfg(dfg, start_activities, end_activities, format='jpg')
    tree = pm4py.discover_process_tree_inductive(log)
    pm4py.view_process_tree(tree, format='jpg')
    net, initial_marking, final_marking = pm4py.convert_to_petri_net(tree)
    pm4py.view_petri_net(net, initial_marking, final_marking, format='jpg')
    bpmn = pm4py.convert_to_bpmn(net, initial_marking, final_marking)
    pm4py.view_bpmn(bpmn, format='jpg')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_analyzer()
