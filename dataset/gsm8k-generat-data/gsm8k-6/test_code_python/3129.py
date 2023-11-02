def solution():
    # Calculate the total amount spent on rose bushes
    total_spent_roses = 6 * 75  # Mike buys 6 rose bushes at 75 dollars each

    # Calculate the total amount spent on tiger tooth aloes
    total_spent_aloes = 2 * 100  # Mike buys 2 tiger tooth aloes for 100 dollars each

    # Calculate the total amount spent on plants for himself
    spent_on_himself = total_spent_roses - (2 * 75) + total_spent_aloes  # Mike bought 2 of the roses for his friend
    result = spent_on_himself
    return result

print(solution())