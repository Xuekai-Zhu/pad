def solution():
    skirts = 3
    pairs_of_pants = 2
    blouses = 5
    skirt_cost = 20
    blouse_cost = 15
    regular_priced_pants = 30
    sale_priced_pants = regular_priced_pants / 2
    total_cost = (skirts * skirt_cost) + (blouses * blouse_cost) + (pairs_of_pants * regular_priced_pants) + (pairs_of_pants * sale_priced_pants)
    result = total_cost
    return result

print(solution())