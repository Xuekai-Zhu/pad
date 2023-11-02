def solution():
    """There are 50 apples and 40 oranges in the cafeteria. If an apple costs $0.80 and an orange costs $0.50, how much does the cafeteria earn for apples and oranges if there are only 10 apples and 6 oranges left?"""
    starting_apples = 50
    starting_oranges = 40
    remaining_apples = 10
    remaining_oranges = 6
    apple_price = 0.8
    orange_price = 0.5
    total_earned = (starting_apples - remaining_apples) * apple_price + (starting_oranges - remaining_oranges) * orange_price
    result = total_earned
    return result

print(solution())