def solution():
    """There are 50 apples and 40 oranges in the cafeteria. If an apple costs $0.80 and an orange costs $0.50, how much does the cafeteria earn for apples and oranges if there are only 10 apples and 6 oranges left?"""
    # Define the initial number of apples and oranges
    initial_apples = 50
    initial_oranges = 40

    # Define the prices of apples and oranges
    apple_price = 0.8
    orange_price = 0.5

    # Define the number of apples and oranges left
    left_apples = 10
    left_oranges = 6

    # Calculate the earnings from selling apples and oranges
    apple_earnings = (initial_apples - left_apples) * apple_price
    orange_earnings = (initial_oranges - left_oranges) * orange_price
    total_earnings = apple_earnings + orange_earnings

    result = total_earnings
    return result

print(solution())