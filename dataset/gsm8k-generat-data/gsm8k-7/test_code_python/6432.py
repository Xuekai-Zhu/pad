def solution():
    marco_money = 24
    mary_money = 15

    # Calculate half of Marco's money
    half_marco_money = marco_money / 2

    # Give half of Marco's money to Mary
    mary_money += half_marco_money

    # Mary spends $5
    mary_money -= 5

    # Calculate the difference between Mary's money and Marco's money
    difference = mary_money - marco_money
    result = difference
    return result

print(solution())