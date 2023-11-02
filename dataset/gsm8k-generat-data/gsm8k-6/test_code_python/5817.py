def solution():
    # Calculate the total amount of money Jenney can make in Neighborhood A
    neighborhood_A_money = 10*2*2  # 10 homes each buy 2 boxes of cookies at $2 per box

    # Calculate the total amount of money Jenney can make in Neighborhood B
    neighborhood_B_money = 5*5*2  # 5 homes each buy 5 boxes of cookies at $2 per box

    # Determine the better choice of the two neighborhoods
    if neighborhood_A_money > neighborhood_B_money:
        result = neighborhood_A_money
    else:
        result = neighborhood_B_money

    return result

print(solution())