def solution():
    flour_needed = 500
    flour_bag_weight = 50
    flour_bag_cost = 20

    salt_needed = 10
    salt_cost = 0.2

    promotion_cost = 1000

    ticket_price = 20
    num_tickets_sold = 500

    # Calculate the total cost of flour
    total_flour_cost = (flour_needed // flour_bag_weight + 1) * flour_bag_cost

    # Calculate the total cost of salt
    total_salt_cost = salt_needed * salt_cost

    # Calculate the total cost of everything (flour, salt, and promotion)
    total_cost = total_flour_cost + total_salt_cost + promotion_cost

    # Calculate the total revenue from ticket sales
    total_revenue = num_tickets_sold * ticket_price

    # Calculate the profit (revenue - cost)
    profit = total_revenue - total_cost
    result = profit
    return result

print(solution())