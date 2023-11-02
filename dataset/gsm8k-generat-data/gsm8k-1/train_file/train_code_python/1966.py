def solution():
    """Guise went to a restaurant and ate ten hot dogs on a Monday. That week, he ate two more dogs each day than the previous day. How many hot dogs had Guise eaten by Wednesday that week?"""
    monday_dogs = 10
    tuesday_dogs = monday_dogs + 2 + 2
    wednesday_dogs = tuesday_dogs + 2 + 2 + 2
    total_dogs = monday_dogs + tuesday_dogs + wednesday_dogs
    result = total_dogs
    return result

print(solution())