def solution():
    """New York recorded 5000 new coronavirus cases on a particular week. In the second week, half as many new coronaviruses cases as the first week was recorded by the state. In the third week, 2000 more cases were recorded in the state. What is the total number of recorded new coronaviruses in the state after the three weeks?"""
    week_1 = 5000
    week_2 = week_1 / 2
    week_3 = week_2 + 2000
    total_cases = week_1 + week_2 + week_3
    result = total_cases
    return result

print(solution())