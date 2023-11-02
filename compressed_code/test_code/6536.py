def solution():
    
    total_price = 67
    coupon = 4
    price_after_coupon = total_price - coupon
    num_people = 3
    each_person_price = price_after_coupon / num_people
    result = each_person_price
    return result

print(solution())