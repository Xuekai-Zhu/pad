def solution():
    """Samuel is driving to San Francisco’s Comic-Con in his car and he needs to travel 600 miles to the hotel where he made a reservation. At first, he drives at 50 miles/hour for 3 hours straight, then he speeds up to 80 miles/hour for 4 hours. How far is he from the hotel?"""
    distance_at_50mph = 50 * 3
    distance_at_80mph = 80 * 4
    total_distance = distance_at_50mph + distance_at_80mph
    distance_left = 600 - total_distance
    result = distance_left
    return result

print(solution())