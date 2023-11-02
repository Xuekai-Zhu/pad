def solution():
    trains_per_birthday = 1  # Max asks for 1 train for every birthday
    trains_per_christmas = 2  # Max asks for 2 trains each Christmas
    years = 5  # Max asks for gifts for 5 years

    # Calculate the total number of trains Max receives over 5 years
    total_trains_received = (trains_per_birthday * 5) + (trains_per_christmas * 10)

    # Calculate the number of trains Max has before receiving double the amount
    trains_before_double = total_trains_received * 5

    # Calculate the number of trains Max has after receiving double the amount
    trains_after_double = trains_before_double * 2

    result = trains_after_double
    return result

print(solution())