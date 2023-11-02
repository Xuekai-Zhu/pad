def solution():
    malik_yards = 18
    josiah_yards = 22
    darnell_avg = 11
    num_games = 4

    # Calculate the total yards rushed by Malik
    malik_total = malik_yards * num_games

    # Calculate the total yards rushed by Josiah
    josiah_total = josiah_yards * num_games

    # Calculate the total yards rushed by Darnell
    darnell_total = darnell_avg * num_games

    # Calculate the total yards rushed by all three athletes
    total_yards = malik_total + josiah_total + darnell_total
    result = total_yards
    return result

print(solution())