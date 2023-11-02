def solution():
    uses_metric_system = True
    uses_metres = False   # initialize as False since we don't know if metres are used yet
    if uses_metric_system:
        uses_metres = True  # if metric system is used, then lengths are measured in metres
    if uses_metres:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())