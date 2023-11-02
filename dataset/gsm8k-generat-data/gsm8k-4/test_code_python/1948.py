def solution():
    """Tonya has opened a lemonade stand selling lemonade in small, medium, and large cups at $1, $2 and $3 respectively. At the close of business she ended up making $50. As she went back through her inventory she noticed that she sold $11 worth of small lemonades and $24 worth of medium lemonades. How many cups of large lemonade did Tonya sell?"""
    # Define the prices of small, medium, and large cups
    small_price = 1
    medium_price = 2
    large_price = 3

    # Define the total amount of money made
    total_money = 50

    # Define the amount of money made from small and medium cups
    small_money = 11
    medium_money = 24

    # Calculate the total number of small and medium cups sold
    small_cups = small_money / small_price
    medium_cups = medium_money / medium_price

    # Calculate the total number of cups sold
    total_cups = small_cups + medium_cups

    # Calculate the total amount of money made from large cups
    large_money = total_money - small_money - medium_money
    # Calculate the number of large cups sold
    large_cups = large_money / large_price

    # return the result
    result = large_cups
    return result

print(solution())