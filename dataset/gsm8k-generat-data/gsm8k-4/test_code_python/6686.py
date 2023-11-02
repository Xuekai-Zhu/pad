def solution():
    """Ashley wants a champagne toast at her wedding. She wants to serve 2 glasses of champagne to each of her 120 wedding guests. 1 bottle of champagne has 6 servings. How many bottles of champagne will she need?"""
    # Define the number of guests and servings per bottle
    num_guests = 120
    servings_per_bottle = 6

    # Calculate the total number of servings necessary
    total_servings = num_guests * 2

    # Calculate the number of bottles needed to serve the champagne
    num_bottles = total_servings / servings_per_bottle

    # Round up to the nearest whole number of bottles
    num_bottles = int(num_bottles) + (num_bottles % 1 > 0)

    result = num_bottles
    return result

print(solution())