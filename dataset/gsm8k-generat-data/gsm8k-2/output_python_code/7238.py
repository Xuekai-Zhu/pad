def solution():
    """Scout delivers groceries on the weekends. His base pay is $10.00 an hour. He also earns a $5.00 tip per customer that he delivers groceries to. On Saturday he worked 4 hours and delivered groceries to 5 people. Sunday he worked 5 hours and delivered groceries to 8 people. How much did he make over the weekend?"""
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