def solution():
    # Calculate the total number of words in the paper
    total_words = 5 * 400

    # Calculate the time it will take Stan to type the paper
    time_in_minutes = total_words / 50

    # Convert the time to hours
    time_in_hours = time_in_minutes / 60

    # Calculate how much water Stan will need to drink
    water_needed = time_in_hours * 15

    result = water_needed
    return result

print(solution())