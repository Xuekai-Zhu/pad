def solution():
    """Nancy wanted to make peanut butter cookies for a family gathering, but her cousin is allergic to peanuts. She decided to make almond butter cookies instead. A jar of almond butter costs three times the amount that a jar of peanut butter does. It takes half a jar to make a batch of cookies. A jar of peanut butter costs $3. How many dollars more does it cost per batch to make almond butter cookies instead of peanut butter cookies?"""
    peanut_butter_price = 3
    almond_butter_price = 3 * 3
    butter_per_batch = 0.5
    cost_per_batch_pb = peanut_butter_price * butter_per_batch
    cost_per_batch_ab = almond_butter_price * butter_per_batch
    difference = cost_per_batch_ab - cost_per_batch_pb
    result = difference
    return result

print(solution())