def solution():
    shirts_per_hour = 4
    pants_per_hour = 3
    hours_ironing_shirts = 3
    hours_ironing_pants = 5
    total_pieces_ironed = (shirts_per_hour * hours_ironing_shirts) + (pants_per_hour * hours_ironing_pants)
    result = total_pieces_ironed
    return result

print(solution())