def solution():
    """A mad scientist created a shrink ray device that, when used on anything, would cause it to shrink by 50%. The scientist, eager to use his new invention, looked through his house for something to shrink zap. The first thing he found and zapped was his wife, who at the time was carrying a tray containing 5 cups filled with coffee. If each coffee cup held 8 ounces of fluid before being zapped, how many ounces of coffee remained after his wife and the cups filled with coffee were shrink zapped?"""
    initial_coffee_ounces = 5 * 8
    remaining_coffee_ounces = initial_coffee_ounces * 0.5
    result = remaining_coffee_ounces
    return result

print(solution())