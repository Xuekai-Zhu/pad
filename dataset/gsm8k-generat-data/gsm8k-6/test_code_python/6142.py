def solution():
    # Calculate the total amount earned from the rooms on each floor
    first_floor_earnings = 15 * 3  # rooms on first floor cost $15 each
    second_floor_earnings = 20 * 3  # rooms on second floor cost $20 each
    third_floor_earnings = (2 * 15) * 2  # rooms on third floor cost twice as much as rooms on first floor, but only 2 rooms are occupied
    total_earnings = first_floor_earnings + second_floor_earnings + third_floor_earnings
    result = total_earnings
    return result

print(solution())