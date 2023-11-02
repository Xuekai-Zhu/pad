def solution():
    """Christine is subbing aquafaba for egg whites in baking.  Every 2 tablespoons of aquafaba is equivalent to 1 egg white.  She's making 2 angel food cakes that call for 8 egg whites each.  How many tablespoons of aquafaba will she need in order not to use egg whites?"""
    # Define the conversion ratio of aquafaba to egg whites
    CONVERSION_RATIO = 2

    # Define the number of egg whites needed for one cake
    egg_whites_per_cake = 8

    # Calculate the total number of egg whites needed for both cakes
    total_egg_whites = egg_whites_per_cake * 2

    # Calculate the equivalent amount of aquafaba needed
    aquafaba_needed = total_egg_whites / CONVERSION_RATIO

    # Display the amount of aquafaba needed
    result = aquafaba_needed
    return result

print(solution())