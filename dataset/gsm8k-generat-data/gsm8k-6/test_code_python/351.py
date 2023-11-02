def solution():
    # Calculate the total number of Wednesdays and Fridays in the school year
    total_days = 5 * 36  # 5 days in a school week
    total_wed_fri = total_days - 3  # Jackson misses 1 Wednesday and 2 Fridays

    # Calculate the total number of peanut butter and jelly sandwiches eaten
    sandwiches = 2 * total_wed_fri  # Jackson eats a sandwich on Wednesdays and Fridays
    result = sandwiches
    return result

print(solution())