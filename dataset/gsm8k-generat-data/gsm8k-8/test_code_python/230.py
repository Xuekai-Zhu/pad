def solution():
    # Define Emery's reading speed ratio to Serena's
    emery_speed_ratio = 5

    # Define the number of days it takes Emery to read the book
    emery_days = 20 / emery_speed_ratio

    # Define the number of days it takes Serena to read the book
    serena_days = 20

    # Calculate the average number of days it takes them to read the book
    average_days = (emery_days + serena_days) / 2

    result = average_days
    return result

print(solution())