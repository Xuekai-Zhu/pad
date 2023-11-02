def solution():
    # Define the number of birds seen on each day
    monday_birds = 70
    tuesday_birds = monday_birds / 2
    wednesday_birds = tuesday_birds + 8

    # Calculate the total number of birds seen
    total_birds = monday_birds + tuesday_birds + wednesday_birds
    result = total_birds
    return result

print(solution())