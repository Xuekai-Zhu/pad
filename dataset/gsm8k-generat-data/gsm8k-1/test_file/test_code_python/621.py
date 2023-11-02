def solution():
    """Arianna plants a garden that has 10 rows of flowers with 20 flowers in each row. Currently, only 4/5 of the planted flowers have bloomed. How many flowers in Arianna's garden have bloomed?"""
    rows = 10
    flowers_per_row = 20
    total_flowers = rows * flowers_per_row
    bloomed_ratio = 4/5
    bloomed_flowers = total_flowers * bloomed_ratio
    result = bloomed_flowers
    return result

print(solution())