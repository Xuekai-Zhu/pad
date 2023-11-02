def solution():
    coal_consumption = 2 # 2 pounds of coal consumed per 5 miles traveled
    remaining_coal = 160 # Given
    distance_traveled = remaining_coal * 5 / coal_consumption # Calculate distance traveled using remaining coal

    result = distance_traveled
    return result

print(solution())