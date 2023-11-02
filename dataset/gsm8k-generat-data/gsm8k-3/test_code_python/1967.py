def solution():
    """Guise went to a restaurant and ate ten hot dogs on a Monday. That week, he ate two more dogs each day than the previous day. How many hot dogs had Guise eaten by Wednesday that week?"""
    # Define the number of hot dogs eaten on Monday
    monday_dogs = 10

    # Calculate the number of hot dogs eaten on Tuesday
    tuesday_dogs = monday_dogs + 2

    # Calculate the number of hot dogs eaten on Wednesday
    wednesday_dogs = tuesday_dogs + 2

    # Calculate the total number of hot dogs eaten
    total_dogs = monday_dogs + tuesday_dogs + wednesday_dogs

    # Display the total number of hot dogs eaten by Wednesday
    result = total_dogs
    return result

print(solution())