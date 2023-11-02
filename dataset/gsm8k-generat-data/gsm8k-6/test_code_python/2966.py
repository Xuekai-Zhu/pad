def solution():
    # Calculate the total amount of Tylenol Mark takes in 12 hours
    dosage = 2 * 500  # each Tylenol tablet has 500 mg
    total_tylenol = dosage * (12 // 4)  # Mark takes the dosage every 4 hours for 12 hours
    total_tylenol_grams = total_tylenol / 1000  # convert mg to grams
    result = total_tylenol_grams
    return result

print(solution())