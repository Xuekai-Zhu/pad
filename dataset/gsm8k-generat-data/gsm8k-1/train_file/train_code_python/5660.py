def solution():
    """The civic league was hosting a pancake breakfast fundraiser. A stack of pancakes was $4.00 and you could add bacon for $2.00. They sold 60 stacks of pancakes and 90 slices of bacon. How much did they raise?"""
    pancakes_price = 4
    bacon_price = 2
    pancakes_sold = 60
    bacon_sold = 90
    total_raised = (pancakes_price * pancakes_sold) + (bacon_price * bacon_sold)
    result = total_raised
    return result

print(solution())