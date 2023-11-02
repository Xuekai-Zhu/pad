def solution():
    """James injured his ankle and decides to slowly start working back up to his previous running goals and then surpass them. Before the injury, he was able to run 100 miles per week. He wants to get up to 20% more than that total in 280 days and each week he will increase miles walked in the week by the same amount. How many miles does he need to add per week?"""
    # Define the initial number of miles per week
    initial_miles = 100

    # Define the target total number of miles
    target_total_miles = initial_miles * 1.2

    # Define the number of days he has to reach his target
    days_left = 280

    # Calculate the number of weeks left
    weeks_left = days_left // 7

    # Calculate the number of miles he needs to add per week to reach his target
    miles_per_week = (target_total_miles - initial_miles) / weeks_left

    result = miles_per_week
    return result

print(solution())