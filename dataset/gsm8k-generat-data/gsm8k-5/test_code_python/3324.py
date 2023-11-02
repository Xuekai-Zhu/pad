def solution():
    total_money = 50  # The initial amount of money given by their mother was $50
    toilet_paper_cost = 12  # The cost of toilet paper was $12
    grocery_cost = 2 * toilet_paper_cost  # They spent twice as much on groceries as on toilet paper
    remaining_money = total_money - toilet_paper_cost - grocery_cost  # Calculate the amount of money left after buying toilet paper and groceries
    money_for_boots = remaining_money / 3  # A pair of boots costs 3 times the amount they had left

    # Calculate the amount of money each girl needs to add to buy two pairs of boots
    additional_money = 2 * money_for_boots - remaining_money
    result = additional_money
    return result

print(solution())