def solution():
    """A mad scientist created a shrink ray device that, when used on anything, would cause it to shrink by 50%. The scientist, eager to use his new invention, looked through his house for something to shrink zap. The first thing he found and zapped was his wife, who at the time was carrying a tray containing 5 cups filled with coffee. If each coffee cup held 8 ounces of fluid before being zapped, how many ounces of coffee remained after his wife and the cups filled with coffee were shrink zapped?"""
    # Define the original amount of coffee in the cups
    original_coffee = 8 * 5

    # Calculate the amount of coffee remaining after the shrink ray is used
    remaining_coffee = original_coffee * 0.5

    # Return the result
    result = remaining_coffee
    return result

print(solution())