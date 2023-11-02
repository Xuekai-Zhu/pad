def solution():
    """Nancy wanted to make peanut butter cookies for a family gathering, but her cousin is allergic to peanuts. She decided to make almond butter cookies instead. A jar of almond butter costs three times the amount that a jar of peanut butter does. It takes half a jar to make a batch of cookies. A jar of peanut butter costs $3. How many dollars more does it cost per batch to make almond butter cookies instead of peanut butter cookies?"""
    peanut_butter_cost = 3
    almond_butter_cost = peanut_butter_cost * 3
    jars_per_batch = 0.5
    cost_per_batch_p = peanut_butter_cost * jars_per_batch
    cost_per_batch_a = almond_butter_cost * jars_per_batch
    cost_difference = cost_per_batch_a - cost_per_batch_p
    result = cost_difference
    return result

print(solution())