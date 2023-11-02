def solution():
    num_figures = 5  # Jimmy has 5 action figures
    normal_value = 15 * 4 + 20  # The normal value of the collection is 4 figures worth $15 and 1 worth $20
    selling_price = normal_value - (5 * num_figures)  # Jimmy is selling each figure for $5 less than its value
    total_earnings = selling_price * num_figures  # Jimmy is selling all 5 figures

    result = total_earnings
    return result

print(solution())