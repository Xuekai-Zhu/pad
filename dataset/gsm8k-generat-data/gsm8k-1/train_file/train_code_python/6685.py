def solution():
    """Ashley wants a champagne toast at her wedding. She wants to serve 2 glasses of champagne to each of her 120 wedding guests. 1 bottle of champagne has 6 servings. How many bottles of champagne will she need?"""
    guests = 120
    servings_per_guest = 2
    servings_per_bottle = 6
    total_servings = guests * servings_per_guest
    total_bottles = total_servings / servings_per_bottle
    result = total_bottles
    return result

print(solution())