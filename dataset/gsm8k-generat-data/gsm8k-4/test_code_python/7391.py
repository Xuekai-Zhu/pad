def solution():
    """At a laundromat, it costs $4 for a washer and a quarter for every 10 minutes in the dryer. Samantha does 2 loads of laundry in the wash and then divides all the washed clothes equally into 3 separate dryers. If she lets the dryers run for 40 minutes each, how much does she spend altogether?"""
    # Define the cost of using the washer and dryer
    washer_cost = 4
    dryer_cost = 0.25

    # Calculate the cost of washing the clothes
    wash_cost = washer_cost * 2

    # Calculate the total drying time needed for all clothes
    total_drying_time = (2 * 45) / 3 # 2 loads of 45 minutes each, divided into 3 dryers

    # Calculate the cost of drying the clothes
    dry_cost = dryer_cost * (total_drying_time / 10) * 3 # 3 dryers running for total_drying_time minutes

    # Calculate the total cost of washing and drying the clothes
    total_cost = wash_cost + dry_cost

    # Return the result as a formatted string
    result = "${:.2f}".format(total_cost)
    return result

print(solution())