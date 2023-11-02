def solution():
    """Jim buys a package of 20 car washes. Since He bought a package he only has to pay 60%. A carwash normally costs 15 dollars. How much did he pay for the package?"""
    num_washes = 20
    regular_price = 15
    discount = 0.6
    price_per_wash = regular_price * discount
    package_price = num_washes * price_per_wash
    result = package_price
    return result

print(solution())