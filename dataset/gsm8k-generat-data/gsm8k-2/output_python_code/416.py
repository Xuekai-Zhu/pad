def solution():
    """Jim buys a package of 20 car washes. Since He bought a package he only has to pay 60%. A carwash normally costs 15 dollars. How much did he pay for the package?"""
    car_wash_price = 15
    package_discount = 0.6
    package_size = 20
    package_price = car_wash_price * package_discount * package_size
    result = package_price
    return result

print(solution())