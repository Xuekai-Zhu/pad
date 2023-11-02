def solution():
    """Each year Dani gets 4 pairs of two pants each as pay winning the best Amazon buyer of the season. If he initially had 50 pants, calculate the number of pants he'll have in 5 years."""
    pants_per_year = 4 * 2
    initial_pants = 50
    total_pants = initial_pants + (pants_per_year * 5)
    result = total_pants
    return result

print(solution())