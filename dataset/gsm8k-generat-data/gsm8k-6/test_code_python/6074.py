def solution():
    # Calculate the number of Legos left in the box
    legos_left = (500 // 2) - 5  # James uses half of the pieces and 5 are missing, so he puts (500 // 2) - 5 pieces back in the box
    result = legos_left
    return result

print(solution())