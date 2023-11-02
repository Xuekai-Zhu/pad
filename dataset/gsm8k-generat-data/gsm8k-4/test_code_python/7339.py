def solution():
    """Brooke is milking cows and then selling the milk at the market for $3 a gallon. Whatever milk doesn't sell, she turns into butter. One gallon of milk equals 2 sticks of butter. She then sells the butter for $1.5 a stick. She has 12 cows. Each cow produces 4 gallons of milk. She has 6 customers, each of whom wants 6 gallons of milk. How much money does she earn if she sells all her milk and butter?"""
    # Define the price of milk and butter
    MILK_PRICE = 3
    BUTTER_PRICE = 1.5

    # Calculate the total gallons of milk produced by all the cows
    total_milk_gallons = 12 * 4

    # Calculate the total gallons of milk needed by the customers
    total_customer_milk = 6 * 6

    # Calculate the total gallons of milk that will be turned into butter
    total_butter_milk = total_milk_gallons - total_customer_milk

    # Calculate the total sticks of butter that will be produced from the milk
    total_butter_sticks = total_butter_milk * 2

    # Calculate the total revenue from selling the milk
    milk_revenue = total_customer_milk * MILK_PRICE

    # Calculate the total revenue from selling the butter
    butter_revenue = total_butter_sticks * BUTTER_PRICE

    # Calculate the total revenue from selling all the milk and butter
    total_revenue = milk_revenue + butter_revenue
    
    result = total_revenue
    return result

print(solution())