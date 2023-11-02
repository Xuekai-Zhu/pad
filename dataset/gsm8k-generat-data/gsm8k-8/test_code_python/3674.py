def solution():
    # Define the total number of attendees
    total_attendees = 120

    # Calculate the number of females
    females = (total_attendees - 4) / 2

    # Calculate the number of males
    males = females + 4

    result = males
    return result

print(solution())