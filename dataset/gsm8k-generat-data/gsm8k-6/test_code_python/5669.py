def solution():
    # Calculate the total cost of keeping the cow for 40 days
    cost_of_food = 20 * 40  # $20 spent every day for 40 days
    total_cost = 600 + cost_of_food + 500  # $600 for buying the cow, $500 for vaccination and deworming, and cost of food

    # Calculate the profit made from selling the cow
    revenue = 2500  # $2500 received from selling the cow after 40 days
    profit = revenue - total_cost  # profit made from selling the cow

    result = profit
    return result

print(solution())