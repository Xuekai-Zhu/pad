def solution():
    """James injured his ankle and decides to slowly start working back up to his previous running goals and then surpass them.  Before the injury, he was able to run 100 miles per week.  He wants to get up to 20% more than that total in 280 days and each week he will increase miles walked in the week by the same amount.  How many miles does he need to add per week?"""
    # Define James' initial weekly miles and his goal percentage increase
    INITIAL_MILES = 100
    GOAL_PERCENTAGE_INCREASE = 0.2

    # Calculate James' goal total miles in 280 days
    goal_total_miles = INITIAL_MILES * (1 + GOAL_PERCENTAGE_INCREASE) * 40

    # Calculate the total additional miles James needs to add over the 280 days
    additional_miles = goal_total_miles - (INITIAL_MILES * 40)

    # Calculate the amount of additional miles James needs to add per week
    additional_miles_per_week = additional_miles / 40

    # Display the amount of additional miles James needs to add per week
    result = additional_miles_per_week
    return result

print(solution())