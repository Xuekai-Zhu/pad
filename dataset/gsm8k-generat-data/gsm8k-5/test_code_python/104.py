def solution():
    # Calculate the number of people the boat can transport in one day
    people_per_day = 4 * 12  # 4 boat trips, each with a capacity of 12 people

    # Calculate the number of people the boat can transport in two days
    people_per_two_days = people_per_day * 2

    result = people_per_two_days
    return result

print(solution())