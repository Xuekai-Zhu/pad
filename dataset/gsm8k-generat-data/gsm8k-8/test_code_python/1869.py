def solution():
    # Calculate the total amount of money Francie saved
    total_savings = 5 * 8 + 6 * 6

    # Calculate the amount of money Francie spent on clothes
    clothes_cost = total_savings / 2

    # Calculate the amount of money Francie has left after buying the video game
    remaining_money = total_savings - clothes_cost - 35
    result = remaining_money
    return result

print(solution())