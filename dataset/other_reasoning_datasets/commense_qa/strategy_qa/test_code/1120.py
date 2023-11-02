def solution():
    osama_islamic_fundamentalist = True
    communion_is_christian_practice = True
    sunday_is_commonly_for_christian_services = True
    if osama_islamic_fundamentalist or not communion_is_christian_practice or not sunday_is_commonly_for_christian_services:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())