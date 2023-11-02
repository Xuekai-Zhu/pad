def solution():
    # Calculate the total volume of soup
    milk = 2  # quarts of milk
    chicken_stock = 3 * 1  # three times as much chicken stock as pureed vegetables (1 quart)
    total_volume = milk + chicken_stock + 1  # 1 quart of pureed vegetables

    # Calculate the number of bags needed
    bags_needed = total_volume // 3  # each bag can hold 3 quarts

    # If there is a remainder, add another bag for the remaining soup
    if total_volume % 3 != 0:
        bags_needed += 1

    result = bags_needed
    return result

print(solution())