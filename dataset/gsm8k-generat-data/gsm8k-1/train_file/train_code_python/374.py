def solution():
    """A store owner buys clothes wholesale and adds 80% to the wholesale price to set the retail price. The retail price of a pair of pants is $36. What is the wholesale price?"""
    retail_price = 36
    markup_percent = 80
    wholesale_price = retail_price / (1 + (markup_percent / 100))
    result = wholesale_price
    return result

print(solution())