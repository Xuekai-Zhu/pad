def solution():
    total_days = 4  # Bill had 4 days to finish the project
    total_hours = total_days * 24  # Calculate the total hours he had available
    nap_hours = 6 * 7  # Bill took a total of 6 seven-hour naps

    # Calculate the total hours Bill spent working on the project
    working_hours = total_hours - nap_hours

    result = working_hours
    return result

print(solution())