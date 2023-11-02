def solution():
    # Calculate the total number of hours James will spend writing
    total_hours = 3  # James writes from 1 PM to 4 PM every night, which is a total of 3 hours

    # Calculate the total number of pages James can write in the given time
    pages_per_hour = 5
    total_pages = pages_per_hour * total_hours

    # Calculate the number of weeks it will take to finish the book
    num_weeks = 735 / total_pages

    result = num_weeks
    return result

print(solution())