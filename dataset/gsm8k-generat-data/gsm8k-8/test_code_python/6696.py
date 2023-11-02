def solution():
    # Define initial amount of sugar
    initial_sugar = 65

    # Calculate amount of sugar after tomorrow
    tomorrow_sugar = initial_sugar - 18

    # Calculate amount of sugar after the following day
    end_sugar = tomorrow_sugar + 50

    result = end_sugar
    return result

print(solution())