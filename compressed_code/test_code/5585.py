def solution():
    
    dress_shirt_cost = 15
    pants_cost = 40
    suit_cost = 150
    sweater_cost = 30
    num_dress_shirts = 4
    num_pants = 2
    num_sweaters = 2
    total_cost = (
        num_dress_shirts * dress_shirt_cost
        + num_pants * pants_cost
        + suit_cost
        + num_sweaters * sweater_cost
    )
    discount = 0.2
    discounted_cost = total_cost - (total_cost * discount)
    coupon_discount = 0.1
    final_cost = discounted_cost - (discounted_cost * coupon_discount)
    result = final_cost
    return result

print(solution())