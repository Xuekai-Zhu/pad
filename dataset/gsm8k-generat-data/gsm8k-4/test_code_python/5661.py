def solution():
    """The civic league was hosting a pancake breakfast fundraiser. A stack of pancakes was $4.00 and you could add bacon for $2.00. They sold 60 stacks of pancakes and 90 slices of bacon. How much did they raise?"""
    # Define the price of a stack of pancakes and the price of bacon
    pancake_price = 4
    bacon_price = 2

    # Calculate the total amount raised from selling pancakes and bacon
    pancake_sales = pancake_price * 60
    bacon_sales = bacon_price * 90
    total_sales = pancake_sales + bacon_sales

    # return the result
    result = total_sales
    return result

print(solution())