def solution():
    """Jake buys 2-pound packages of sausages. He buys 3 of them and they are $4 a pound. How much does he pay?"""
    # Define the price per pound and the number of packages
    sausages_price = 4
    num_packages = 3

    # Calculate the total weight of sausages purchased
    total_weight = num_packages * 2

    # Calculate the total cost of the sausages
    total_cost = total_weight * sausages_price

    # return the result
    result = total_cost
    return result

print(solution())