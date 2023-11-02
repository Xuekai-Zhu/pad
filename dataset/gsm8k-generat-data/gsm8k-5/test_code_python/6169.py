def solution():
    total_distance = 26.3  # The marathon is 26.3 miles
    current_distance = 3  # Tomas can run 3 miles during the first month of training
    num_of_months = 1  # Keep track of the number of months it takes to reach the marathon distance

    # Keep doubling the distance Tomas can run each month until he can run the full marathon distance
    while current_distance < total_distance:
        current_distance *= 2
        num_of_months += 1

    result = num_of_months
    return result

print(solution())