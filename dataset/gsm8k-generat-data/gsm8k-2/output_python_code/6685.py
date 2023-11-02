def solution():
    """Ashley wants a champagne toast at her wedding. She wants to serve 2 glasses of champagne to each of her 120 wedding guests. 1 bottle of champagne has 6 servings. How many bottles of champagne will she need?"""
    guests = 120
    glasses_per_guest = 2
    total_glasses = guests * glasses_per_guest
    servings_per_bottle = 6
    bottles_needed = total_glasses / servings_per_bottle
    result = bottles_needed
    return result

print(solution())