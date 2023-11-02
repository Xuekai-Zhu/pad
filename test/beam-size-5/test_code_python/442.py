def solution():
    eggs_in_cases = 4 * 12  # Rozanne uses 4 dozen eggs that were in cases
    eggs_lost_in_cupboard = 2  # Rozanne uses 2 eggs that were loose in the cupboard
    eggs_per_glass = 5  # Each glass needs 5 eggs

    # Calculate the total number of eggs Rozanne can make
    total_eggs = eggs_in_cases + eggs_lost_in_cupboard

    # Calculate the number of trays Rozanne can put out
    trays = total_eggs // eggs_per_glass
    result = trays
    return result

print(solution())