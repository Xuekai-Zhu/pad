def solution():
    # Calculate Sean's money
    sean_money = (1/2) * 40 + 4  # Sean has 4 dollars more than half as much money as Fritz
    # Calculate Rick's money
    rick_money = 3 * sean_money  # Rick has 3 times as much money as Sean
    # Calculate total money of Sean and Rick
    total_money = sean_money + rick_money
    result = total_money
    return result

print(solution())