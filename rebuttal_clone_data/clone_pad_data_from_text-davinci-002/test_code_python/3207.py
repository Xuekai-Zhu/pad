def solution():
     # the total number of liters sold is 3 + 2 + 5 = 10
    containers_filled = 3 + 2 + 5
    # each container was filled with a different amount of milk
    # so we need to sum up the total amount of milk sold
    # 3 containers * 2 liters each = 6 liters
    # 2 containers * 0.75 liters each = 1.5 liters
    # 5 containers * 0.5 liters each = 2.5 liters
    # 6 + 1.5 + 2.5 = 10 liters
    total_milk_sold = 6 + 1.5 + 2.5
    result = total_milk_sold
    return result

print(solution())