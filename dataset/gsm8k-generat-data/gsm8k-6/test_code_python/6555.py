def solution():
    # Calculate how many miles James wants to run in 280 days
    goal_miles = 100 * 1.2  # James wants to run 20% more than his previous goal of 100 miles per week
    weeks = 280 // 7  # Convert days to weeks
    previous_week_miles = 100 // 7  # Calculate how many miles James previously ran per week
    # Calculate how many miles James needs to add to his weekly mileage to reach his goal
    added_miles_per_week = (goal_miles - 100) / weeks - previous_week_miles
    result = added_miles_per_week
    return result

print(solution())