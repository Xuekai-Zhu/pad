def solution():
    """At a people counting station, the number of people counted on the first day was twice the total number counted on the second day. If 500 people were counted on the second day, how many people were counted on the two days?"""
    second_day_count = 500
    first_day_count = 2 * second_day_count
    total_count = first_day_count + second_day_count
    result = total_count
    return result

print(solution())