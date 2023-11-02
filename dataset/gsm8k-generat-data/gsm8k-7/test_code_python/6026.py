def solution():
    num_boxes = 3
    num_burritos_per_box = 20
    given_away_fraction = 1/3
    num_days = 10
    num_burritos_per_day = 3

    # Calculate the total number of burritos that John bought
    total_burritos = num_boxes * num_burritos_per_box

    # Calculate the number of burritos that John gave away to his friend
    given_away_burritos = total_burritos * given_away_fraction

    # Calculate the number of burritos that John will eat
    eaten_burritos = num_days * num_burritos_per_day

    # Calculate the number of burritos that John has left
    remaining_burritos = total_burritos - given_away_burritos - eaten_burritos
    result = remaining_burritos
    return result

print(solution())