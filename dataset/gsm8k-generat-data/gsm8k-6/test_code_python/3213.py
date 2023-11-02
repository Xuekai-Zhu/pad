def solution():
    # Calculate the total money made from selling pumpkin and custard pies
    pumpkin_slices = 8 * 4  # each pumpkin pie is cut into 8 pieces and she sells 4 pies
    custard_slices = 6 * 5  # each custard pie is cut into 6 pieces and she sells 5 pies
    total_money = (pumpkin_slices * 5) + (custard_slices * 6)  # pumpkin pie is $5 a slice, custard pie is $6 a slice

    result = total_money
    return result

print(solution())