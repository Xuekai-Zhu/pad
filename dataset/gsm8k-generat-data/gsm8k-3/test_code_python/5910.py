def solution():
    """A mad scientist created a shrink ray device that, when used on anything, would cause it to shrink by 50%.  The scientist, eager to use his new invention, looked through his house for something to shrink zap.  The first thing he found and zapped was his wife, who at the time was carrying a tray containing 5 cups filled with coffee.  If each coffee cup held 8 ounces of fluid before being zapped, how many ounces of coffee remained after his wife and the cups filled with coffee were shrink zapped?"""
    # Define the initial amount of coffee
    initial_coffee = 5 * 8 # 5 cups x 8 ounces/cup

    # Apply the shrink ray device twice to reduce the amount of coffee by 50% each time
    final_coffee = initial_coffee * 0.5 * 0.5

    # Display the final amount of coffee
    result = final_coffee
    return result

print(solution())