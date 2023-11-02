def solution():
    shirt_cost = 15
    num_shirts = 4
    pants_cost = 40
    num_pants = 2
    suit_cost = 150
    num_suits = 1
    sweater_cost = 30
    num_sweaters = 2
    store_discount = 20
    coupon_discount = 10
    shirts_total = shirt_cost * num_shirts
    pants_total = pants_cost * num_pants
    suit_total = suit_cost * num_suits
    sweater_total = sweater_cost * num_sweaters
    total_cost = shirts_total + pants_total + suit_total + sweater_total
    store_discount_amount = total_cost * (store_discount / 100)
    total_after_store_discount = total_cost - store_discount_amount
    total_after_coupon = total_after_store_discount * (1 - (coupon_discount / 100))
    result = total_after_coupon
    
    return result

print(solution())