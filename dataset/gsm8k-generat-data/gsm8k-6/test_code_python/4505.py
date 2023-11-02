def solution():
    # Calculate the total number of arrests during the protests
    total_arrests = 21 * 30 * 10  # 21 different cities, 30 days of protests, 10 arrests per day in each city

    # Calculate the total time spent in jail by each arrested person
    jail_time_per_person = 4 + 7  # 4 days before trial + half of a 14-day sentence

    # Calculate the total combined weeks of jail time 
    combined_jail_time = (total_arrests * jail_time_per_person) / 7  # divide by 7 to convert days to weeks

    result = combined_jail_time
    return result

print(solution())