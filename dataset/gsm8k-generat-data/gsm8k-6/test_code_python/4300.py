def solution():
    # Calculate the total hours Anie can work in a day, including the 5 extra hours
    total_hours = 10 + 5  # her normal work schedule requires her to be productive for 10 hours, and she needs 5 extra hours

    # Calculate the number of days it would take Anie to complete the project
    days = 1500 / total_hours  # divide the total number of hours by the total number of hours she can work per day

    result = days
    return result

print(solution())