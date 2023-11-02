def solution():
    """Steve has a bank account that earns 10% interest every year. He puts $100 in it, and then 10 each year. How much money is in it after two years?"""
    total_money = 100
    interest_rate = 0.1
    for year in range(1, 3):
        total_money += 10 #annual deposit
        total_money += total_money * interest_rate #annual interest
    result = total_money
    return result

print(solution())