def solution():
    orchids_sold = 20
    orchid_price = 50
    chinese_plants_sold = 15
    chinese_plant_price = 25

    # Calculate the total amount earned from orchid sales
    orchid_earnings = orchids_sold * orchid_price  

    # Calculate the total amount earned from Chinese plant sales
    chinese_plant_earnings = chinese_plants_sold * chinese_plant_price  

    # Calculate the total expenses (worker salaries and new pot purchases)
    total_expenses = (2 * 40) + 150  

    # Calculate the total earnings
    total_earnings = orchid_earnings + chinese_plant_earnings  

    # Calculate the final amount left after expenses
    amount_left = total_earnings - total_expenses  
    result = amount_left
    return result

print(solution())