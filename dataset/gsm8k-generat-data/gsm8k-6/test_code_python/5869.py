def solution():
    # Calculate the total number of toy cars Jaden has
    total_cars = 14 + 28 + 12  # 14 cars originally, 28 bought from store, 12 received as birthday gifts
    # Calculate the number of toy cars Jaden gave away
    given_cars = 8 + 3  # 8 to his sister, 3 to his friend Vinnie
    # Calculate the remaining number of toy cars Jaden has
    remaining_cars = total_cars - given_cars
    result = remaining_cars
    return result

print(solution())