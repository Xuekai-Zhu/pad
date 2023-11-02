def solution():
    """Melanie is making meatballs for dinner. The recipe calls for breadcrumbs. To make the breadcrumbs Melanie is going to tear 2 slices of bread into smaller pieces and then add them to a blender to grind them into fine crumbs. First she tears the bread slices each in half, then tears those halves in half. How many bread pieces is Melanie going to put into the blender?"""
    # Define the number of bread slices
    bread_slices = 2

    # Tear each bread slice in half
    bread_halves = bread_slices * 2

    # Tear each bread half in half
    bread_pieces = bread_halves * 2

    # return the result
    result = bread_pieces
    return result

print(solution())