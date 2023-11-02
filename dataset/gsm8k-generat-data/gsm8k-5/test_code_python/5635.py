def solution():
    total_weight = 10 * 200  # Mr. Ray has a total of 2000 pounds of tuna
    pounds_per_customer = 25  # Each customer wants 25 pounds of tuna
    customers_served = total_weight // pounds_per_customer  # Calculate the number of customers served
    customers_unserved = 100 - customers_served  # Calculate the number of unserved customers
    result = customers_unserved
    return result

print(solution())