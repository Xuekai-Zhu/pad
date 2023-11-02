def solution():
    """Bret takes a 9 hour train ride to go to Boston. He spends 2 hours reading a book, 1 hour to eat his dinner, and 3 hours watching movies on his computer. How many hours does he have left to take a nap?"""
    # Define the total hours of the train ride and the time spent on activities
    total_hours = 9
    activity_hours = 2 + 1 + 3

    # Calculate the remaining hours for napping
    nap_hours = total_hours - activity_hours

    # Return the result
    result = nap_hours
    return result

print(solution())