def solution():
    """Melanie is making meatballs for dinner. The recipe calls for breadcrumbs. To make the breadcrumbs Melanie is going to tear 2 slices of bread into smaller pieces and then add them to a blender to grind them into fine crumbs. First she tears the bread slices each in half, then tears those halves in half. How many bread pieces is Melanie going to put into the blender?"""
    slices_of_bread = 2
    num_pieces = (2 ** 2) * slices_of_bread
    result = num_pieces
    return result

print(solution())