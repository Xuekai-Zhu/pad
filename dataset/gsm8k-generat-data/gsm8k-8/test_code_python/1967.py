def solution():
    # Define Guise's hot dog consumption each day
    monday = 10
    tuesday = monday + 2
    wednesday = tuesday + 2 + 2

    # Calculate the total number of hot dogs eaten by Wednesday
    total_hot_dogs = monday + tuesday + wednesday
    result = total_hot_dogs
    return result

print(solution())