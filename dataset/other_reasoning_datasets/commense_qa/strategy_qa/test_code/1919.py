def solution():
    # Define the professions and events
    railroad_engineer = "Railroad engineer"
    nascar_event = "NASCAR event"
    # Check if a railroad engineer is needed during NASCAR events
    if railroad_engineer not in nascar_event:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())