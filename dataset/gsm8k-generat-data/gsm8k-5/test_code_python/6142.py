def solution():
    # Calculate the monthly earnings from the first floor
    first_floor_earnings = 15 * 3  # There are 3 rooms on the first floor at $15 per month

    # Calculate the monthly earnings from the second floor
    second_floor_earnings = 20 * 3  # There are 3 rooms on the second floor at $20 per month

    # Calculate the monthly earnings from the third floor
    third_floor_earnings = 2 * (15 * 2)  # There are 2 rooms on the third floor at twice the rate of the first floor

    # Calculate the total monthly earnings
    total_earnings = first_floor_earnings + second_floor_earnings + third_floor_earnings
    result = total_earnings
    return result

print(solution())