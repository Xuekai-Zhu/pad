def solution():
    shoes_cost = 74
    socks_cost = 2
    num_pairs_of_socks = 2
    bag_cost = 42
    discount_threshold = 100
    discount_percent = 0.1

    # Calculate the total cost of all items
    total_cost = shoes_cost + (num_pairs_of_socks * socks_cost) + bag_cost

    # Calculate the amount exceeding $100 of the total cost
    amount_above_discount_threshold = max(total_cost - discount_threshold, 0)

    # Calculate the discount amount
    discount_amount = amount_above_discount_threshold * discount_percent

    # Calculate the total amount to be paid after discount
    total_amount_paid = total_cost - discount_amount

    result = total_amount_paid
    return result

print(solution())