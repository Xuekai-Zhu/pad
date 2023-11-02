def solution():
    # Calculate the number of bottles filled for the football team
    football_bottles = 11 * 6

    # Calculate the number of bottles filled for the lacrosse team
    lacrosse_bottles = football_bottles + 12

    # Calculate the total number of bottles for all teams
    total_bottles = football_bottles + 53 + lacrosse_bottles + 2 + 2 + 2

    # Calculate the number of bottles filled for the rugby team
    rugby_bottles = 254 - total_bottles

    result = rugby_bottles
    return result

print(solution())