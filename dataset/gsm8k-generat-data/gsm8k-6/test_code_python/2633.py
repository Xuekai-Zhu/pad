def solution():
    # Calculate the total number of birds seen from Monday to Wednesday
    monday_birds = 70
    tuesday_birds = monday_birds / 2
    wednesday_birds = tuesday_birds + 8
    total_birds = monday_birds + tuesday_birds + wednesday_birds
    result = total_birds
    return result

print(solution())