def solution():
    pocket_money = 450  # Joe's pocket money is $450
    chocolates_spent = pocket_money * (1/9)  # Joe spent 1/9 of his money on chocolates
    fruits_spent = pocket_money * (2/5)  # Joe spent 2/5 of his money on fruits

    # Calculate the total money spent
    total_spent = chocolates_spent + fruits_spent

    # Calculate the money left
    money_left = pocket_money - total_spent
    result = money_left
    return result

print(solution())