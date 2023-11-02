def solution():
    total_brownies = 24  # Tina made a pan of 24 brownies
    eaten_by_tina = 2 * 5  # Tina ate 2 brownies per day for 5 days
    eaten_by_husband = 5  # Tina's husband ate 1 brownie per day for 5 days
    shared_with_guests = 4  # Tina shared 4 brownies with guests

    # Calculate the total number of brownies left
    brownies_left = total_brownies - eaten_by_tina - eaten_by_husband - shared_with_guests
    result = brownies_left
    return result

print(solution())