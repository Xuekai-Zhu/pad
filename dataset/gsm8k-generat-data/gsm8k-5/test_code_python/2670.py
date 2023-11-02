def solution():
    people_second_day = 500  # 500 people were counted on the second day
    people_first_day = 2 * people_second_day  # The number of people counted on the first day was twice the total number counted on the second day

    # Calculate the total number of people counted on the two days
    total_people_counted = people_first_day + people_second_day
    result = total_people_counted
    return result

print(solution())