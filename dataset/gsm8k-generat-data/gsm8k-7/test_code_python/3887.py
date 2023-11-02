def solution():
    total_weekly_miles = 70
    first_dog_avg_miles = 2
    num_days = 7

    # Calculate the total miles walked by the first dog in a week
    first_dog_weekly_miles = first_dog_avg_miles * num_days

    # Calculate the total miles walked by the second dog in a week
    second_dog_weekly_miles = total_weekly_miles - first_dog_weekly_miles

    # Calculate the average number of miles walked by the second dog per day
    second_dog_avg_miles = second_dog_weekly_miles / num_days
    result = second_dog_avg_miles
    return result

print(solution())