def solution():
    """In a shopping mall, one T-shirt costs $20 each; a pair of pants costs $80; a pair of shoes costs $150. All items will get a 10% discount. How much does Eugene have to pay if he buys four T-shirts, three pairs of pants, and two pairs of shoes?"""
    tshirt_cost = 20
    pants_cost = 80
    shoes_cost = 150
    num_tshirts = 4
    num_pants = 3
    num_shoes = 2

    total_cost = (tshirt_cost * num_tshirts) + (pants_cost * num_pants) + (shoes_cost * num_shoes)
    discount = total_cost * 0.10
    total_cost_after_discount = total_cost - discount
    
    result = total_cost_after_discount
    
    return result

print(solution())