def solution():
    # Calculate the number of hard hats remaining after Carl and John took some away
    pink_remaining = 26 - 4 - 6  # Carl took away 4 and John took away 6
    green_remaining = 15 - 2*6  # John took away twice as many green hats as he took pink hats
    yellow_remaining = 24
    total_remaining = pink_remaining + green_remaining + yellow_remaining
    result = total_remaining
    return result

print(solution())