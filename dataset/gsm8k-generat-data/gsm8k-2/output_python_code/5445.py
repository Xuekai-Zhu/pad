def solution():
    """A building has 10 floors. It takes 15 seconds to go up the stairs to the even-numbered floors and 9 seconds to go up to the odd-numbered floors.
    This includes getting to the first floor. How many minutes does it take to get to the 10th floor?"""
    even_floor_time = 15
    odd_floor_time = 9
    total_floors = 10
    total_time = 0
    for i in range(1, total_floors + 1):
        if i % 2 == 0:
            total_time += even_floor_time
        else:
            total_time += odd_floor_time
    total_time /= 60 #converts to minutes
    result = total_time
    return result

print(solution())