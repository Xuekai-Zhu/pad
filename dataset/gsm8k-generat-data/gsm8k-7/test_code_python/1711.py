def solution():
    adult_price = 30
    child_price = adult_price / 2  # Half price
    num_adults = 10 - 4  # Subtract the number of children to get number of adults
    num_children = 4
    soda_price = 5
    discount = 0.2  # 20% discount

    # Calculate the total cost of adult tickets
    total_adult_cost = num_adults * adult_price

    # Calculate the total cost of child tickets
    total_child_cost = num_children * child_price

    # Calculate the total cost before the soda discount
    total_cost_before_discount = total_adult_cost + total_child_cost

    # Calculate the discounted price after applying the soda discount
    discounted_price = total_cost_before_discount * (1 - discount)

    # Add the cost of the soda to the discounted price
    total_cost = discounted_price + soda_price
    result = total_cost
    return result

print(solution())