def solution():
    """Danny brings 3 watermelons to his family picnic. He cuts each watermelon into 10 slices. His sister brings 1 watermelon to the family picnic, and she cuts the watermelon into 15 slices. How many watermelon slices are there in total at the picnic?"""
    danny_watermelons = 3
    danny_slices_per_watermelon = 10
    sister_watermelons = 1
    sister_slices_per_watermelon = 15
    total_slices = (danny_watermelons * danny_slices_per_watermelon) + (sister_watermelons * sister_slices_per_watermelon)
    result = total_slices
    return result

print(solution())