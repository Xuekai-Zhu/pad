def solution():
    """Ashley's pizza delivery costs $15. What is the total amount that Ashley should give the delivery man if she wants to give a tip that is equal to 1/5 of the amount she ordered?"""
    order_amount = 15
    tip_percentage = 0.2
    tip_amount = order_amount * tip_percentage
    total_amount = order_amount + tip_amount
    result = total_amount
    
    return result

print(solution())