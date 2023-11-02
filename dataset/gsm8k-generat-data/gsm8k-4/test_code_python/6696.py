def solution():
    """Jack has 65 pounds of sugar today. Tomorrow he will use 18 pounds of sugar and the following day he will buy 50 more pounds of sugar. How many pounds will he have in the end?"""
    # Define the initial number of pounds of sugar
    initial_sugar = 65

    # Calculate the number of pounds of sugar he will have after using 18 pounds
    sugar_after_use = initial_sugar - 18

    # Calculate the number of pounds of sugar he will have after buying 50 more pounds
    final_sugar = sugar_after_use + 50

    result = final_sugar
    return result

print(solution())