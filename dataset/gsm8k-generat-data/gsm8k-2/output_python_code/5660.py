def solution():
    """The civic league was hosting a pancake breakfast fundraiser. A stack of pancakes was $4.00 and you could add bacon for $2.00. They sold 60 stacks of pancakes and 90 slices of bacon. How much did they raise?"""
    pancake_price = 4
    bacon_price = 2
    pancake_sales = 60
    bacon_sales = 90
    total_sales = (pancake_price * pancake_sales) + (bacon_price * bacon_sales)
    result = total_sales
    return result

print(solution())