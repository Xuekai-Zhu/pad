def solution():
    """Jake buys 2-pound packages of sausages. He buys 3 of them and they are $4 a pound. How much does he pay?"""
    package_weight = 2
    num_packages = 3
    price_per_pound = 4
    total_weight = package_weight * num_packages
    total_price = total_weight * price_per_pound
    result = total_price
    return result

print(solution())