def solution():
    """Rachel and Sara want to attend a beauty and modeling contest. They both want to buy new pairs of shoes and dresses. 
    Sara buys a pair of shoes which costs $50 and a dress which costs $200.
    How much should Rachel budget if she wants to spend twice as much as what Sara spent on the pair of shoes and dress?"""
    sara_shoes_price = 50
    sara_dress_price = 200
    sara_total_price = sara_shoes_price + sara_dress_price
    rachel_total_price = 2 * sara_total_price
    result = rachel_total_price
    return result

print(solution())