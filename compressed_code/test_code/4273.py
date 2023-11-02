def solution():
    
    bike_price = 2345
    current_savings = 1500
    lawn_income = 20 * 20
    newspaper_income = 0.4 * 600
    dog_income = 15 * 24
    total_income = lawn_income + newspaper_income + dog_income
    total_savings = current_savings + total_income
    money_left = total_savings - bike_price
    result = money_left
    return result

print(solution())