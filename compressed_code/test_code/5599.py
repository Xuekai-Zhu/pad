def solution():
    
    base_pay = 10
    tip_per_delivery = 5
    saturday_hours = 4
    saturday_deliveries = 5
    sunday_hours = 5
    sunday_deliveries = 8

    saturday_earnings = (base_pay * saturday_hours) + (tip_per_delivery * saturday_deliveries)
    sunday_earnings = (base_pay * sunday_hours) + (tip_per_delivery * sunday_deliveries)

    total_earnings = saturday_earnings + sunday_earnings
    result = total_earnings
    return result

print(solution())