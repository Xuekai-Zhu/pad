def solution():
    """At a laundromat, it costs $4 for a washer and a quarter for every 10 minutes in the dryer. Samantha does 2 loads of laundry in the wash and then divides all the washed clothes equally into 3 separate dryers. If she lets the dryers run for 40 minutes each, how much does she spend altogether?"""
    cost_per_washer = 4
    cost_per_dryer = 0.25 * 4  # $0.25 for every 10 minutes, so $1 for 40 minutes
    num_washers = 2
    num_dryers = 3
    total_cost = (cost_per_washer * num_washers) + (cost_per_dryer * num_dryers)
    result = total_cost
    return result

print(solution())