def solution():
    """Jack has 65 pounds of sugar today. Tomorrow he will use 18 pounds of sugar and the following day he will buy 50 more pounds of sugar. How many pounds will he have in the end?"""
    # Define the initial amount of sugar
    initial_sugar = 65

    # Calculate the amount of sugar left after using 18 pounds
    sugar_left = initial_sugar - 18

    # Calculate the amount of sugar he will have after buying 50 pounds
    total_sugar = sugar_left + 50

    # Display the total amount of sugar
    result = total_sugar
    return result

print(solution())