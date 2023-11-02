def solution():
    """Mr. Ray has 100 customers waiting at his fish market. He has 10 tuna, each of which weighs 200 pounds. Each customer wants 25 pounds of tuna. Mr. Ray's store is first come, first served. How many customers will go home without any fish?"""
    total_tuna_weight = 10 * 200
    tuna_per_customer = 25
    max_customers_served = total_tuna_weight // tuna_per_customer
    customers_without_fish = 100 - max_customers_served
    result = customers_without_fish
    return result

print(solution())