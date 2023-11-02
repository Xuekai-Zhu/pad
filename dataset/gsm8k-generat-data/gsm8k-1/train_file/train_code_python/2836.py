def solution():
    """Ali is a baker. Leila ordered 3 chocolate cakes for $12 each and 6 strawberry cakes for $22 each. How much should Leila pay Ali?"""
    num_choc_cakes = 3
    choc_cake_price = 12
    num_straw_cakes = 6
    straw_cake_price = 22
    total_price = (num_choc_cakes * choc_cake_price) + (num_straw_cakes * straw_cake_price)
    result = total_price
    return result

print(solution())