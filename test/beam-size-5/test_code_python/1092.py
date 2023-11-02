def solution():
    # Calculate the number of people Billy can help in one day
    people_per_day = 2 * 3  # Billy can help 2 people per hour for 3 hours a day

    # Calculate the total number of people Billy can help in one day
    people_per_day = people_per_day * 31  # 31 days in March

    # Calculate the number of people Billy takes for March 1st and April 19th off
    people_between_1st_and_april = people_per_day * 0.8  # 20% of the days between March 1st and April 19th off

    # Calculate the total number of people Billy can help in all the days
    total_people = people_per_day + people_between_1st_and_april
    result = total_people
    return result

print(solution())