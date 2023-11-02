def solution():
    sandwich_cost = 8
    coupon_discount = sandwich_cost * 0.25
    upgraded_cost = sandwich_cost + 1
    total_cost = upgraded_cost + 3
    drink_cost = total_cost - (upgraded_cost + coupon_discount)
    result = drink_cost
    return result

print(solution())