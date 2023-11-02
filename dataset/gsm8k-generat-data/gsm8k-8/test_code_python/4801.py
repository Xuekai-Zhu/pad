def solution():
    # Calculate total hours Tom runs each week
    total_hours = 5 * 1.5

    # Convert hours to minutes
    total_minutes = total_hours * 60

    # Calculate total distance ran in miles
    speed = 8 # mph
    distance = speed * (total_minutes / 60)
    result = distance
    return result

print(solution())