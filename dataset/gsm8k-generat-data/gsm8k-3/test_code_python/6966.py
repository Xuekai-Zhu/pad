def solution():
    """Darnell pays $12 for unlimited texting and calling on his phone each month.
    An alternative phone plan would charge $1 per 30 texts and $3 per 20 minutes of calls per month.
    Darnell sends 60 texts and spends 60 minutes on the phone each month.
    How many dollars less would he pay on the alternative plan?"""
    # Calculate Darnell's cost on his current plan
    current_cost = 12

    # Calculate the cost on the alternative plan
    text_cost = 2  # 60 texts / 30 texts per dollar = 2 dollars
    call_cost = 9  # 60 minutes / 20 minutes per dollar = 3 dollars per 20 minutes = 9 dollars
    alternative_cost = text_cost + call_cost

    # Calculate the difference between the two plans
    difference = current_cost - alternative_cost

    # Display the difference in cost
    result = difference
    return result

print(solution())