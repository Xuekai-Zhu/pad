def solution():
    # Calculate the total number of tablets taken
    num_tablets = 12 // 4 * 2

    # Calculate the total amount of Tylenol taken in milligrams
    total_tylenol_mg = num_tablets * 500

    # Convert the total Tylenol taken to grams
    total_tylenol_g = total_tylenol_mg / 1000

    result = total_tylenol_g
    return result

print(solution())