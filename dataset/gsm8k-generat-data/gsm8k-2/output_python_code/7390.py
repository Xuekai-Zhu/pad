def solution():
    """At a laundromat, it costs $4 for a washer and a quarter for every 10 minutes in the dryer. Samantha does 2 loads of laundry in the wash and then divides all the washed clothes equally into 3 separate dryers. If she lets the dryers run for 40 minutes each, how much does she spend altogether?"""
    washer_cost = 4
    dryer_cost = 0.25 / 6  # per minute
    wash_loads = 2
    dryers = 3
    dryer_time = 40  # minutes
    total_cost = (washer_cost * wash_loads) + (dryer_cost * dryers * dryer_time)
    result = total_cost
    return result

print(solution())