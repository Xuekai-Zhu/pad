def solution():
    duck1_bread = 0.5
    duck2_bread = 13
    duck3_bread = 7
    remaining_bread = 30

    # Calculate the total amount of bread the first duck ate
    duck1_eaten = duck1_bread * (duck2_bread + duck3_bread + remaining_bread)

    # Calculate the total amount of bread all the ducks ate
    total_eaten = duck1_eaten + duck2_bread + duck3_bread + remaining_bread

    # Calculate the total amount of bread that was thrown in the pond
    total_bread = total_eaten / duck1_bread
    result = total_bread
    return result

print(solution())