def solution():
    # Calculate the total money Aaron and Carson had
    total_money = 40 + 40

    # Calculate the bill for dinner
    dinner_bill = 0.75 * total_money

    # Calculate the total amount they spent on ice cream
    total_ice_cream_cost = total_money - dinner_bill - 2  # 2 dollars for change

    # Calculate how many scoops they each bought
    num_scoops_each = int(total_ice_cream_cost / 3)

    result = num_scoops_each
    return result

print(solution())