def solution():
    """Rachel and Sara want to attend a beauty and modeling contest. They both want to buy new pairs of shoes and dresses. Sara buys a pair of shoes which costs $50 and a dress which costs $200. How much should Rachel budget if she wants to spend twice as much as what Sara spent on the pair of shoes and dress?"""
    sara_shoes = 50
    sara_dress = 200
    sara_total = sara_shoes + sara_dress
    rachel_total = sara_total * 2
    result = rachel_total
    return result

print(solution())