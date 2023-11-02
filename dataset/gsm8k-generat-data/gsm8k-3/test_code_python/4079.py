def solution():
    """Clare's mother gave her $47 to go to the store. Clare bought 4 loaves of bread and 2 cartons of milk. Each loaf of bread cost $2 and each carton of milk cost $2. How much money does Clare have left?"""
    # Define the cost of each item
    BREAD_PRICE = 2
    MILK_PRICE = 2

    # Define the number of each item purchased
    bread_count = 4
    milk_count = 2

    # Calculate the total cost of the bread and milk
    total_cost = (bread_count * BREAD_PRICE) + (milk_count * MILK_PRICE)

    # Calculate the amount of money Clare has left
    money_left = 47 - total_cost

    # Display the amount of money Clare has left
    result = money_left
    return result

print(solution())