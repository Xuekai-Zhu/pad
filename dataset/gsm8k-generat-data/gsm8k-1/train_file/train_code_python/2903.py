def solution():
    """Mark spent 220 dollars to fix his car. It needed two parts that cost 20 dollars each, and labor cost .5 dollars a minute. How many hours did the mechanic work?"""
    part_cost = 20
    labor_cost_per_min = 0.5
    labor_time_in_mins = (220 - (2 * part_cost)) / labor_cost_per_min
    labor_time_in_hours = labor_time_in_mins / 60
    result = labor_time_in_hours
    return result

print(solution())