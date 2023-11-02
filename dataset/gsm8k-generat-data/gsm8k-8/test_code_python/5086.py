def solution():
    # Define the regular prices
    ticket_price = 10
    food_combo_price = 10

    # Calculate the discounted prices during the special offer
    discounted_ticket_price = ticket_price * 0.8
    discounted_food_combo_price = food_combo_price * 0.5

    # Calculate the total cost of going to the movies with and without the discount
    total_cost_without_discount = ticket_price + food_combo_price
    total_cost_with_discount = discounted_ticket_price + discounted_food_combo_price

    # Calculate the amount of money Trip could save with the discount
    savings = total_cost_without_discount - total_cost_with_discount
    result = savings
    return result

print(solution())