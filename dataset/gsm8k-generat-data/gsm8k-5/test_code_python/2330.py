def solution():
    mural_area = 20 * 15  # Calculate the total area of the mural in square feet
    time_taken = mural_area * 20  # Calculate the time taken to paint the mural in minutes

    # Calculate the total cost of painting the mural
    cost = (time_taken / 60) * 150  # Convert the time taken to hours and multiply by hourly rate
    result = cost
    return result

print(solution())