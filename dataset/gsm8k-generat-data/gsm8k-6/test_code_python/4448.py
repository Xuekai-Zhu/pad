def solution():
    # Calculate the total number of bottles filled for football team
    football_bottles = 11 * 6

    # Calculate the total number of bottles filled for lacrosse team
    lacrosse_bottles = football_bottles + 12

    # Calculate the total number of bottles filled for coaches
    coaches_bottles = 4 * 2  # 4 teams in total

    # Calculate the number of bottles filled for rugby team
    rugby_bottles = 254 - football_bottles - soccer_bottles - lacrosse_bottles - coaches_bottles
    result = rugby_bottles
    return result

print(solution())