def solution():
    """Nancy wanted to make peanut butter cookies for a family gathering, but her cousin is allergic to peanuts. She decided to make almond butter cookies instead. A jar of almond butter costs three times the amount that a jar of peanut butter does. It takes half a jar to make a batch of cookies. A jar of peanut butter costs $3. How many dollars more does it cost per batch to make almond butter cookies instead of peanut butter cookies?"""
    # Define the cost of a jar of peanut butter and the ratio of the cost of almond butter to peanut butter
    peanut_butter_cost = 3
    almond_peanut_ratio = 3

    # Calculate the cost of a jar of almond butter
    almond_butter_cost = peanut_butter_cost * almond_peanut_ratio

    # Calculate the cost difference between using almond butter and peanut butter
    cost_difference = almond_butter_cost - peanut_butter_cost

    # Calculate the cost of making a batch of almond butter cookies
    almond_cookie_cost = cost_difference / 2

    # return the result
    result = almond_cookie_cost
    return result

print(solution())