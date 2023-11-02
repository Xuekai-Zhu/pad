def solution():
    # Calculate how much money Michael's brother had after receiving half of the money
    brother_money = (1/2) * 42  # half of Michael's money
    brother_money -= 3  # brother buys 3 dollars worth of candy
    final_money = 35  # brother has 35 dollars left
    initial_money = brother_money + final_money  # calculate initial amount of money
    result = initial_money
    return result

print(solution())