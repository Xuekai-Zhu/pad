def solution():
    total_miles = 20  # Rosie wants to run 20 miles for the week
    miles_ran = 6 * (1 + 1 + 1 + (30/60) + (20/60))  # Rosie has already ran for a total of 6 miles per hour on different days
    miles_remaining = total_miles - miles_ran  # Rosie has to run the remaining distance
    remaining_time = (20/60) * ((miles_remaining / 6) * 60)  # Calculate the time required to run the remaining distance

    # Convert the remaining time to minutes
    remaining_minutes = int(remaining_time % 60)
    result = remaining_minutes
    return result

print(solution())