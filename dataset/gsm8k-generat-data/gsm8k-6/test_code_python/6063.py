def solution():
    # Calculate the number of dishes Megan can prepare in 2 hours
    total_time = 2 * 60  # convert 2 hours to minutes
    time_per_dish = 20
    dishes = total_time // time_per_dish

    # Calculate the number of people Megan can feed
    people = dishes * 5
    result = people
    return result

print(solution())