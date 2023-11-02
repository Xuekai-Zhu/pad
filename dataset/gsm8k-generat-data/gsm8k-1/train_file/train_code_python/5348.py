def solution():
    """Samuel is driving to San Francisco’s Comic-Con in his car and he needs to travel 600 miles to the hotel where he made a reservation. At first, he drives at 50 miles/hour for 3 hours straight, then he speeds up to 80 miles/hour for 4 hours. How far is he from the hotel?"""
    initial_speed = 50
    initial_time = 3
    final_speed = 80
    final_time = 4
    distance_covered = (initial_speed * initial_time) + (final_speed * final_time)
    distance_left = 600 - distance_covered
    result = distance_left
    return result

print(solution())