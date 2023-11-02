def solution():
     renter_payment = 400
     monthly_rent = 900
     num_renters = 3
     monthly_profit = monthly_rent - (num_renters * renter_payment)
     yearly_profit = monthly_profit * 12
     result = yearly_profit
     return result

print(solution())