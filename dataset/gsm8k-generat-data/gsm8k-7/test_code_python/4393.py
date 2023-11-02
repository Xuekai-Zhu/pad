def solution():
    prize_money = 150
    painting_price = 50
    num_paintings_sold = 3

    # Calculate the total amount of money Hallie makes from selling her paintings
    painting_income = painting_price * num_paintings_sold

    # Calculate the total amount of money Hallie makes from the art contest prize and selling her paintings
    total_income = prize_money + painting_income
    result = total_income
    return result

print(solution())