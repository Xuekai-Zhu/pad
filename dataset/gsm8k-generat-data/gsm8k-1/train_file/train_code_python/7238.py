def solution():
    """Scout delivers groceries on the weekends. His base pay is $10.00 an hour. He also earns a $5.00 tip per customer that he delivers groceries to. On Saturday he worked 4 hours and delivered groceries to 5 people. Sunday he worked 5 hours and delivered groceries to 8 people. How much did he make over the weekend?"""
    base_pay = 10
    tip = 5
    saturday_hours = 4
    saturday_customers = 5
    sunday_hours = 5
    sunday_customers = 8
    saturday_pay = base_pay * saturday_hours
    sunday_pay = base_pay * sunday_hours
    saturday_tip = saturday_customers * tip
    sunday_tip = sunday_customers * tip
    total_pay = saturday_pay + sunday_pay + saturday_tip + sunday_tip
    result = total_pay
    return result

print(solution())