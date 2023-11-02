def solution():
    initial_cost = 600  # Jett bought the cow for $600
    daily_food_cost = 20  # Jett spent $20 every day to buy food for the cow
    medical_cost = 500  # Jett spent $500 on vaccination and deworming

    total_cost = initial_cost + (daily_food_cost * 40) + medical_cost  # Calculate the total cost of owning the cow for 40 days

    selling_price = 2500  # Jett sold the cow for $2500 after 40 days

    profit = selling_price - total_cost  # Calculate the profit Jett made from selling the cow

    result = profit
    return result

print(solution())