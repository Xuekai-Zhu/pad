def solution():
    num_orchids = 20
    orchid_price = 50
    num_chinese_money_plant = 15
    chinese_money_plant_price = 25
    num_workers = 2
    worker_salary = 40
    pot_price = 150

    # Calculate the total earnings from selling the orchids and Chinese money plant
    total_earnings = (num_orchids * orchid_price) + (num_chinese_money_plant * chinese_money_plant_price)

    # Calculate the total amount spent on workers' salaries
    total_worker_salary = num_workers * worker_salary

    # Calculate the total amount spent on buying new pots
    total_pot_price = pot_price

    # Calculate the total expenses
    total_expenses = total_worker_salary + total_pot_price

    # Calculate the remaining earnings after expenses
    remaining_earnings = total_earnings - total_expenses
    result = remaining_earnings
    return result

print(solution())