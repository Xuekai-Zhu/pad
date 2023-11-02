def solution():
    """Ashley wants a champagne toast at her wedding. She wants to serve 2 glasses of champagne to each of her 120 wedding guests. 1 bottle of champagne has 6 servings. How many bottles of champagne will she need?"""
    # Define the number of guests and glasses per guest
    NUM_GUESTS = 120
    GLASSES_PER_GUEST = 2

    # Calculate the total number of glasses needed
    total_glasses = NUM_GUESTS * GLASSES_PER_GUEST

    # Calculate the number of bottles needed
    BOTTLE_SERVINGS = 6
    bottles = total_glasses / BOTTLE_SERVINGS

    # Round up to the nearest whole bottle
    bottles = math.ceil(bottles)

    # Display the number of bottles needed
    result = bottles
    return result

print(solution())