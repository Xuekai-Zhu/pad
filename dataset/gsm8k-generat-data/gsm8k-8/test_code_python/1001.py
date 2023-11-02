def solution():
    # Calculate the total earnings from selling orchids and Chinese money plants
    orchid_sales = 20 * 50
    chinese_plant_sales = 15 * 25
    total_sales = orchid_sales + chinese_plant_sales

    # Calculate the total expenses for paying the workers and buying new pots
    worker_expenses = 2 * 40
    pot_expenses = 150
    total_expenses = worker_expenses + pot_expenses

    # Calculate the remaining earnings after expenses
    remaining_earnings = total_sales - total_expenses
    result = remaining_earnings
    return result

print(solution())