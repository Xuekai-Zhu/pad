def solution():
    # Calculate the total weight of tuna available
    total_weight = 10 * 200  # 10 tuna, each weighing 200 pounds

    # Calculate the number of customers who will receive fish
    customers_served = min(total_weight // 25, 100)  # minimum of total_weight divided by 25 and 100, as there are only 100 customers

    # Calculate the number of customers who will go home empty-handed
    customers_without_fish = 100 - customers_served

    result = customers_without_fish
    return result

print(solution())