def solution():
    # Calculate the cost of one cheesecake
    cheesecake_cost = 12 * 1.25 / 4  # one cheesecake is 25% cheaper than the apple pie

    # Calculate the cost of the muffins
    muffin_cost = 2 * cheesecake_cost * 2  # the six-pack of muffins was two times more expensive than the cheesecake

    # Calculate the total cost of the food
    total_cost = 2 * cheesecake_cost + muffin_cost + 12 # Natalie bought two cheesecakes, an apple pie, and a six-pack of muffins

    result = total_cost
    return result

print(solution())