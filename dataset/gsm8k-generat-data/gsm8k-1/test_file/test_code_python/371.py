def solution():
    """Mrs. Sherman made a dozen bread rolls for breakfast. After feeding her 6 children with one each, she broke each of the remaining rolls into 8 pieces and fed them to the chickens. How many pieces of rolls did she feed to the chickens?"""
    rolls = 12
    children = 6
    remaining_rolls = rolls - children
    pieces_per_roll = 8
    pieces_fed_to_chickens = remaining_rolls * pieces_per_roll
    result = pieces_fed_to_chickens
    return result

print(solution())