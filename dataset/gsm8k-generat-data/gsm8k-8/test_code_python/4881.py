def solution():
    # Define the spending ratios
    snap_to_crackle_ratio = 2
    crackle_to_pop_ratio = 3

    # Calculate the total spending
    total_spending = 150

    # Calculate the sum of the ratios in order to find the value of one ratio
    total_ratio = snap_to_crackle_ratio + 1 + crackle_to_pop_ratio

    # Calculate the value of one ratio
    one_ratio = total_spending / total_ratio

    # Calculate Pop's spending
    pop_spending = one_ratio

    result = pop_spending
    return result

print(solution())