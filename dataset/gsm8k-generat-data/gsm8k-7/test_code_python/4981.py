def solution():
    akeno_spending = 2985
    lev_spending = akeno_spending / 3
    ambrocio_spending = lev_spending - 177

    # Calculate the total spending of Lev and Ambrocio combined
    total_spending_of_other_two = lev_spending + ambrocio_spending

    # Calculate how much more Akeno spent than the other two
    diff = akeno_spending - total_spending_of_other_two
    result = diff
    return result

print(solution())