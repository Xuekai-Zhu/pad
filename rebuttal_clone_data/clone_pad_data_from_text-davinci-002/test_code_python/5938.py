def solution():
    regular_price = 120
     membership_discount = 10
     coupon_discount = 10
     after_membership_discount = regular_price - (regular_price * (membership_discount / 100))
     after_coupon_discount = after_membership_discount - coupon_discount
     result = after_coupon_discount
     
     return result

print(solution())