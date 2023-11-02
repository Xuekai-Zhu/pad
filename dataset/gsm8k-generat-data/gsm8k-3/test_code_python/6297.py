def solution():
    """Jordan decides to start an exercise program when he weighs 250 pounds.  For the first 4 weeks, he loses 3 pounds a week.  After that, he loses 2 pounds a week for 8 weeks.  How much does Jordan now weigh?"""
    # Define Jordan's starting weight and weight loss rates
    starting_weight = 250
    rate1 = 3
    rate2 = 2

    # Define the number of weeks for each weight loss rate
    weeks1 = 4
    weeks2 = 8

    # Calculate Jordan's weight after 4 weeks
    weight1 = starting_weight - rate1 * weeks1

    # Calculate Jordan's weight after 8 more weeks
    weight2 = weight1 - rate2 * weeks2

    # Display Jordan's current weight
    result = weight2
    return result

print(solution())