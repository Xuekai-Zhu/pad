def solution():
    
    milk_per_cow = 4
    number_of_cows = 12
    number_of_customers = 6
    milk_needed = number_of_customers * 6
    milk_leftover = milk_per_cow * number_of_cows - milk_needed
    butter_made = milk_leftover / 2
    milk_sold = milk_needed
    price_per_gallon = 3
    price_per_stick = 1.5
    income_milk = milk_sold * price_per_gallon
    income_butter = butter_made * price_per_stick
    total_income = income_milk + income_butter
    result = total_income
    
    return result

print(solution())