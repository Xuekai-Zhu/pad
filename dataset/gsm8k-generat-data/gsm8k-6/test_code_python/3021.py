def solution():
    # Calculate the total weight of the paper used
    total_paper_weight = 8 * (1/5)  # 8 pieces of paper that weigh 1/5 of an ounce each

    # Calculate the total weight of the letter
    total_letter_weight = total_paper_weight + (2/5)  # paper weight + envelope weight

    # Calculate the number of stamps needed
    stamps_needed = total_letter_weight // 1  # each stamp covers 1 ounce
    result = stamps_needed
    return result

print(solution())