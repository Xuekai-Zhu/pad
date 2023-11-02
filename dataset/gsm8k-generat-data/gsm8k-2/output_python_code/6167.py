def solution():
    """There are 50 apples and 40 oranges in the cafeteria. If an apple costs $0.80 and an orange costs $0.50, how much does the cafeteria earn for apples and oranges if there are only 10 apples and 6 oranges left?"""
    apple_count = 50
    orange_count = 40
    apple_price = 0.8
    orange_price = 0.5
    remaining_apples = 10
    remaining_oranges = 6
    total_earnings = (apple_count - remaining_apples) * apple_price + (orange_count - remaining_oranges) * orange_price
    result = total_earnings
    return result

print(solution())