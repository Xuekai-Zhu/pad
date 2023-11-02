def solution(): 
    """Natalie bought some food for a party she is organizing. She bought two cheesecakes, an apple pie, and a six-pack of muffins. The six-pack of muffins was two times more expensive than the cheesecake, and one cheesecake was only 25% cheaper than the apple pie. If the apple pie cost $12, how much did Natalie pay for all her shopping?"""
    apple_pie_cost = 12
    cheesecake_cost = apple_pie_cost / 0.75
    muffin_cost = 2 * cheesecake_cost
    total_cost = (2 * cheesecake_cost) + apple_pie_cost + muffin_cost
    result = total_cost
    return result

print(solution())