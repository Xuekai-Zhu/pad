def solution():
    """Darnell pays $12 for unlimited texting and calling on his phone each month. An alternative phone plan would charge $1 per 30 texts and $3 per 20 minutes of calls per month. Darnell sends 60 texts and spends 60 minutes on the phone each month. How many dollars less would he pay on the alternative plan?"""
    # Define the cost of Darnell's current phone plan
    current_cost = 12

    # Calculate the cost of the alternative phone plan
    alternative_cost = (60/30) * 1 + (60/20) * 3

    # Calculate the amount saved by switching to the alternative phone plan
    saved_amount = current_cost - alternative_cost

    # Return the result
    result = saved_amount
    return result

print(solution())