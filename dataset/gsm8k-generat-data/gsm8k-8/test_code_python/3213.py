def solution():
    # Calculate the total money made from pumpkin pies
    pumpkin_slices = 8 * 4
    pumpkin_money = pumpkin_slices * 5

    # Calculate the total money made from custard pies
    custard_slices = 6 * 5
    custard_money = custard_slices * 6

    # Calculate the total money made from all sales
    total_money = pumpkin_money + custard_money
    result = total_money
    return result

print(solution())