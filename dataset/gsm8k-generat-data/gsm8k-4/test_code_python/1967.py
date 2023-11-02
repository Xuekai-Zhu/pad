def solution():
    """Guise went to a restaurant and ate ten hot dogs on a Monday. That week, he ate two more dogs each day than the previous day. How many hot dogs had Guise eaten by Wednesday that week?"""
    # Define the initial number of hot dogs eaten on Monday
    monday_hotdogs = 10

    # Calculate the number of hot dogs eaten on Tuesday and Wednesday
    tuesday_hotdogs = monday_hotdogs + 2
    wednesday_hotdogs = tuesday_hotdogs + 2

    # Calculate the total number of hot dogs eaten by Wednesday
    total_hotdogs = monday_hotdogs + tuesday_hotdogs + wednesday_hotdogs

    # return the result
    result = total_hotdogs
    return result

print(solution())