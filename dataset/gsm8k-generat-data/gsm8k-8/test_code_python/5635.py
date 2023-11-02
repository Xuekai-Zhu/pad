def solution():
    # Calculate the total amount of tuna available
    total_tuna = 10 * 200

    # Calculate the number of customers that can be served with the available tuna
    customers_served = total_tuna // 25

    # Calculate the number of customers who will go home without any fish
    customers_left = 100 - customers_served

    result = customers_left
    return result

print(solution())