def solution():
    # Calculate the number of people that can be transported in one day
    people_per_day = 4 * 12  # 4 trips with a capacity of 12 people each

    # Calculate the number of people that can be transported in 2 days
    people_per_two_days = people_per_day * 2

    result = people_per_two_days
    return result

print(solution())