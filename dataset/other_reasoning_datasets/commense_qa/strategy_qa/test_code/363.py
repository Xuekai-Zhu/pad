def solution():
    lymphoma = "serious type of cancer"
    tumors_in_lymph_nodes = "can begin with tumors in the lymph nodes"
    when_untreated = "can kill when left untreated"
    if tumors_in_lymph_nodes and when_untreated:
        result = "no, tumors in the lymph nodes are not ignorable"
    else:
        result = "yes, tumors in the lymph nodes can be ignored"
    return result

print(solution())