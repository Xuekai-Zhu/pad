def solution():
    # Calculate the weight lost by the second person
    weight_lost_2 = 27 - 7  # the second person lost 7 kilograms less than the first person

    # Calculate the weight lost by the remaining two people
    weight_lost_remaining = (103 - 27 - weight_lost_2) / 2  # the remaining two people lost the same amount

    result = weight_lost_remaining
    return result

print(solution())