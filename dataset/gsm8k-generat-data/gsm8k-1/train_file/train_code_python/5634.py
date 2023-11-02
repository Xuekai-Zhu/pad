def solution():
    """Mr. Ray has 100 customers waiting at his fish market. He has 10 tuna, each of which weighs 200 pounds. Each customer wants 25 pounds of tuna. Mr. Ray's store is first come, first served. How many customers will go home without any fish?"""
    total_tuna_weight = 10 * 200
    amount_of_customers_served = total_tuna_weight // 25
    customers_left_without_fish = 100 - amount_of_customers_served
    result = customers_left_without_fish
    return result

print(solution())