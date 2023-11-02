def solution():
    """Nancy wanted to make peanut butter cookies for a family gathering, but her cousin is allergic to peanuts. She decided to make almond butter cookies instead. A jar of almond butter costs three times the amount that a jar of peanut butter does. It takes half a jar to make a batch of cookies. A jar of peanut butter costs $3. How many dollars more does it cost per batch to make almond butter cookies instead of peanut butter cookies?"""
    # Define the cost of a jar of peanut butter and a jar of almond butter
    PEANUT_BUTTER_PRICE = 3
    ALMOND_BUTTER_PRICE = 3 * 3

    # Define the amount of butter needed to make a batch of cookies
    BUTTER_PER_BATCH = 0.5

    # Calculate the cost of butter per batch for peanut butter cookies
    peanut_butter_cost_per_batch = PEANUT_BUTTER_PRICE * BUTTER_PER_BATCH

    # Calculate the cost of butter per batch for almond butter cookies
    almond_butter_cost_per_batch = ALMOND_BUTTER_PRICE * BUTTER_PER_BATCH

    # Calculate the difference in cost per batch between almond butter and peanut butter cookies
    cost_difference_per_batch = almond_butter_cost_per_batch - peanut_butter_cost_per_batch

    # Display the difference in cost per batch
    result = cost_difference_per_batch
    return result

print(solution())