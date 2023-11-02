def solution():
    """Martin went on an eight-hour business trip. During the first half of the trip, he traveled at a speed of 70 kilometers per hour and during the second half at a speed of 85 kilometers per hour. How many kilometers did he travel during the journey?"""
    total_time = 8
    first_half_time = total_time / 2
    second_half_time = total_time / 2
    first_half_distance = 70 * first_half_time
    second_half_distance = 85 * second_half_time
    total_distance = first_half_distance + second_half_distance
    result = total_distance
    return result

print(solution())