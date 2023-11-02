def solution():
    """At a laundromat, it costs $4 for a washer and a quarter for every 10 minutes in the dryer. Samantha does 2 loads of laundry in the wash and then divides all the washed clothes equally into 3 separate dryers. If she lets the dryers run for 40 minutes each, how much does she spend altogether?"""
    # Define the cost of each washer and dryer use
    WASHER_PRICE = 4
    DRYER_PRICE = 0.25
    DRYER_TIME = 40 # in minutes

    # Calculate the total cost for washer use
    washer_cost = WASHER_PRICE * 2

    # Calculate the total cost for dryer use
    total_dryer_time = DRYER_TIME * 3 # in minutes
    dryer_cost = (total_dryer_time // 10) * DRYER_PRICE

    # Calculate the total cost for both washer and dryer use
    total_cost = washer_cost + dryer_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())