def solution():
    # Calculate the total area of the mural
    mural_area = 20 * 15

    # Calculate the time it takes to paint the mural in minutes
    time_in_minutes = mural_area * 20

    # Convert the time to hours
    time_in_hours = time_in_minutes / 60

    # Calculate the total cost of painting the mural
    total_cost = time_in_hours * 150

    result = total_cost
    return result

print(solution())