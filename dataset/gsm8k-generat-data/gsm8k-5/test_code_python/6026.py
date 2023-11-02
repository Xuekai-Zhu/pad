def solution():
    num_boxes = 3  # John buys 3 boxes of burritos
    burritos_per_box = 20  # Each box has 20 burritos
    total_burritos = num_boxes * burritos_per_box  # Calculate the total number of burritos

    # John gives away a third of the burritos
    given_away = total_burritos // 3

    # John eats 3 burritos per day for 10 days
    eaten = 3 * 10

    # Calculate the remaining burritos
    remaining = total_burritos - given_away - eaten
    result = remaining
    return result

print(solution())