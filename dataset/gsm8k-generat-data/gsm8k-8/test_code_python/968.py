def solution():
    # Calculate half of Mary's blue shirts and a third of her brown shirts
    blue_give_away = 26 / 2
    brown_give_away = 36 / 3

    # Subtract the given away shirts from the original amounts
    blue_left = 26 - blue_give_away
    brown_left = 36 - brown_give_away

    # Calculate the total number of shirts left
    total_left = blue_left + brown_left
    result = total_left
    return result

print(solution())