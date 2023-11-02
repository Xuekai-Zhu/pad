def solution():
    """A certain company is in the business of selling fresh fruit. One crate of such fruit consists of 5 bananas, 12 apples, and 7 oranges. The price for such a crate depends on the price of its individual fruits. One apple costs $0.5 and one banana costs twice as much. Oranges are the most expensive and cost three times as much as a banana per piece. What would be the price for such a crate of fruit?"""
    bananas = 5
    apples = 12
    oranges = 7
    apple_price = 0.5
    banana_price = apple_price * 2
    orange_price = banana_price * 3
    total_price = (bananas * banana_price) + (apples * apple_price) + (oranges * orange_price)
    result = total_price
    return result

print(solution())