def solution():
    """There are 50 apples and 40 oranges in the cafeteria. If an apple costs $0.80 and an orange costs $0.50, how much does the cafeteria earn for apples and oranges if there are only 10 apples and 6 oranges left?"""
    # Define the initial number of apples and oranges
    initial_apples = 50
    initial_oranges = 40

    # Define the cost per apple and per orange
    apple_cost = 0.8
    orange_cost = 0.5

    # Calculate the earnings from the apples and oranges sold
    sold_apples = initial_apples - 10
    sold_oranges = initial_oranges - 6
    earnings = (sold_apples * apple_cost) + (sold_oranges * orange_cost)

    # Display the cafeteria's earnings
    result = earnings
    return result

print(solution())