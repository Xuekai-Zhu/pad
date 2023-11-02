def solution():
    """Clare's mother gave her $47 to go to the store. Clare bought 4 loaves of bread and 2 cartons of milk. Each loaf of bread cost $2 and each carton of milk cost $2. How much money does Clare have left?"""
    # Define the initial amount of money given to Clare
    initial_money = 47

    # Calculate the cost of the loaves of bread and cartons of milk
    bread_cost = 4 * 2
    milk_cost = 2 * 2

    # Calculate the total cost of Clare's purchases
    total_cost = bread_cost + milk_cost

    # Calculate the money left after the purchases
    money_left = initial_money - total_cost
    result = money_left
    return result

print(solution())