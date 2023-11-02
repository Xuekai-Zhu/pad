def solution():
    """Manny has a tree that grows at the rate of fifty centimeters every two weeks. If the tree is currently 2 meters tall, how tall, in centimeters, will the tree be in 4 months?"""
    # Define the initial height of the tree in centimeters
    height_cm = 200

    # Calculate the growth rate of the tree in centimeters per week
    growth_rate_cm_week = 25

    # Calculate the total number of weeks in 4 months
    weeks_4_months = 16

    # Calculate the total growth of the tree in centimeters
    total_growth_cm = growth_rate_cm_week * weeks_4_months

    # Calculate the final height of the tree in centimeters
    final_height_cm = height_cm + total_growth_cm

    # return the result
    result = final_height_cm
    return result

print(solution())