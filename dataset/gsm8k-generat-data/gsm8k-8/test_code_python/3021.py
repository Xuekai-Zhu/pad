def solution():
    # Calculate the total weight of the paper
    paper_weight = 8 * (1/5)

    # Calculate the total weight of the letter
    letter_weight = paper_weight + (2/5)

    # Calculate the number of stamps needed (1 stamp per ounce)
    stamps_needed = letter_weight * 1

    result = stamps_needed
    return result

print(solution())