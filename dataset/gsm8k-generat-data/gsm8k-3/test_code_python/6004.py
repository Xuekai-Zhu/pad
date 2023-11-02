def solution():
    """It takes 50 large jelly beans to fill up a large drinking glass.  It takes half that amount to fill up a small drinking glass.  If there are 5 large drinking glasses and 3 small ones, how many jellybeans will it take to fill them up?"""
    # Define the number of jelly beans needed for a large and small glass
    LARGE_GLASS = 50
    SMALL_GLASS = LARGE_GLASS / 2

    # Define the number of large and small glasses
    num_large_glasses = 5
    num_small_glasses = 3

    # Calculate the total number of jelly beans needed
    total_jellybeans = num_large_glasses * LARGE_GLASS + num_small_glasses * SMALL_GLASS

    # Display the total number of jelly beans needed
    result = total_jellybeans
    return result

print(solution())