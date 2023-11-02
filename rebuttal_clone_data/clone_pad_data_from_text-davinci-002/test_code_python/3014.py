def solution():
    bowls_delivered = 638
    bowls_lost = 12
    bowls_broken = 15
    bowls_delivered_safely = bowls_delivered - bowls_lost - bowls_broken
    fee = 100
    payment_per_safe_bowl = 3
    payment_per_broken_bowl = 4
    total_payment = fee + (bowls_delivered_safely * payment_per_safe_bowl) - (bowls_broken * payment_per_broken_bowl)
    result = total_payment
    return result

print(solution())