def solution():
    # Calculate the total cost of textbooks
    cost_on_sale = 5 * 10  # Marta bought 5 textbooks on sale for $10 each
    cost_online = 40  # Marta ordered 2 textbooks online for a total of $40
    cost_bookstore = 3 * cost_online  # Marta bought 3 textbooks from the bookstore for a total of 3 times the cost of online ordered books
    total_cost = cost_on_sale + cost_online + cost_bookstore
    result = total_cost
    return result

print(solution())