def solution():
    num_patrons_cars = 12
    num_patrons_bus = 27

    # Calculate the total number of patrons who need to be transported from the overflow lot
    total_patrons = num_patrons_cars + num_patrons_bus

    # Calculate the number of golf carts needed to transport all patrons
    num_golf_carts = (total_patrons // 3) + (1 if total_patrons % 3 != 0 else 0)
    result = num_golf_carts
    return result

print(solution())