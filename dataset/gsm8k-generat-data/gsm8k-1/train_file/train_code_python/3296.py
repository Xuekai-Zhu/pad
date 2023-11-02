def solution():
    """Tom's puts 30 miles per day on his bike for the first 183 days of the year. For the rest of the days of the year he goes 35 miles per day. How many miles does he drive for the year?"""
    first_half_days = 183
    second_half_days = 365 - first_half_days
    first_half_distance = 30 * first_half_days
    second_half_distance = 35 * second_half_days
    total_distance = first_half_distance + second_half_distance
    result = total_distance
    return result

print(solution())