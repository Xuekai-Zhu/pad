def solution():
    """John visits three different countries. He stays in the first country for 2 weeks and he spends twice as long in each of the other two countries. How much time does he spend on the trip?"""
    first_country_time = 2 * 7  # 2 weeks converted to days
    second_country_time = 2 * first_country_time
    third_country_time = second_country_time
    total_time = first_country_time + second_country_time + third_country_time
    result = total_time
    return result

print(solution())