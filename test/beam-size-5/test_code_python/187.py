def solution():
    insects_per_week = 3.5  # Ducks need 3.5 pounds of insects each week to survive
    ducks = 10  # There are 10 ducks in the flock
    days_per_week = 7  # There are 7 days in a week

    # Calculate the total amount of insects needed per day
    total_insects_per_day = ducks * insects_per_week * days_per_week
    result = total_insects_per_day
    return result

print(solution())