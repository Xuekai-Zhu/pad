def solution():
    gallons_per_minute = 20
    total_gallons_needed = 4000
    firefighters = 5

    # Calculate the total gallons of water that can be delivered per minute by the team of firefighters
    total_gallons_per_minute = gallons_per_minute * firefighters

    # Calculate the time it will take to deliver the total gallons needed
    time_in_minutes = total_gallons_needed / total_gallons_per_minute
    result = time_in_minutes
    return result

print(solution())