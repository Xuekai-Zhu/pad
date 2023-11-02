def solution():
    # Calculate the amount of money George donated to charity
    donated_money = monthly_income / 2  

    # Calculate the amount of money George spent on groceries
    grocery_money = 20

    # Calculate the amount of money George had left after his donations and grocery expenses
    remaining_money = 100

    # Calculate the monthly income of George
    monthly_income = (donated_money + grocery_money + remaining_money) * 2
    
    result = monthly_income
    return result

print(solution())