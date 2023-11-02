def solution():
    """Nate is feeding his livestock hay. Each goat needs 5 pounds, and each sheep needs 3 pounds less than twice the amount each goat needs. If there are 15 goats and 12 sheep, how many pounds of hay does Nate need?"""
    goat_hay = 5
    sheep_hay = 2 * goat_hay - 3
    total_goat_hay = goat_hay * 15
    total_sheep_hay = sheep_hay * 12
    total_hay = total_goat_hay + total_sheep_hay
    result = total_hay
    return result

print(solution())