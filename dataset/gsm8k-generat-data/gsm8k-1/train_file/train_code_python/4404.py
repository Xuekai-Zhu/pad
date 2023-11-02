def solution():
    """Matt rode his bike away from the house, he rode a total of 1000 feet. Along the way, he passed a stop sign that was 350 feet away from his house. He continued his ride and passed a second sign. After passing the second sign he rode an additional 275 feet. How many feet are between the first and second signs?"""
    total_distance = 1000
    distance_to_first_sign = 350
    distance_after_second_sign = 275
    distance_between_signs = total_distance - (distance_to_first_sign + distance_after_second_sign)
    result = distance_between_signs
    return result

print(solution())