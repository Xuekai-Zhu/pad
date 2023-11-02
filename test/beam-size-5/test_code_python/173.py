def solution():
    salary = 6000  # Zaid earns 6000$ per month
    rent = salary * (1/4)  # Zaid spends 1/4 of his salary on rent
    car_fuel = salary * (1/3)  # Zaid spends 1/3 of his salary on car fuel
    remaining = salary - rent - car_fuel  # Zaid has this much money left after expenses and car fuel donations
    daughter_money = 200  # Zaid gives his daughter money to his wife
    remaining -= daughter_money  # Zaid donates half of the remaining amount to his favorite charity
    remaining -= 700  # Zaid gives his daughter money to his wife for groceries and other household goods

    # Calculate Zaid's remaining money after all expenses and donations
    remaining_money = remaining - remaining_money
    result = remaining_money
    return result

print(solution())