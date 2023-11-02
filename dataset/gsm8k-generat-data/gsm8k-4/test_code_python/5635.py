def solution():
    """Mr. Ray has 100 customers waiting at his fish market. He has 10 tuna, each of which weighs 200 pounds. Each customer wants 25 pounds of tuna. Mr. Ray's store is first come, first served. How many customers will go home without any fish?"""
    # Define the number of customers and tuna
    num_customers = 100
    num_tuna = 10
    tuna_weight = 200

    # Calculate the total weight of tuna available
    total_tuna_weight = num_tuna * tuna_weight

    # Calculate the number of customers who can be served
    max_customers = total_tuna_weight // 25

    # Find the number of customers who will go home without any fish
    customers_without_fish = num_customers - max_customers

    # Return the result
    result = customers_without_fish
    return result

print(solution())