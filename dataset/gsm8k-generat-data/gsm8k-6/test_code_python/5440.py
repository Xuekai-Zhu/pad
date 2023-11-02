def solution():
    # Calculate the total amount saved in n weeks, where n is the number of weeks it takes Jaime to save $135
    total_saved = 0
    weeks = 0
    while total_saved < 135:
        weeks += 1
        total_saved += 50
        if weeks % 2 == 0:
            total_saved -= 46  # every two weeks she spends $46 on lunch
    result = weeks
    return result

print(solution())