def solution():
    # Define the cost of the gift, cake, and the amount saved by Erika and Rick
    gift_cost = 250
    cake_cost = 25
    erika_money = 155
    rick_money = 0.5 * gift_cost

    # Calculate the total amount of money they have
    total_money = erika_money + rick_money

    # Calculate the total cost of the gift and cake
    total_cost = gift_cost + cake_cost

    # Calculate the amount left after buying the gift and cake
    left_over = total_money - total_cost
    result = left_over
    return result

print(solution())