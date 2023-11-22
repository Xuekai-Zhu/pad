def solution():
    
    num_cds = 10
    CD_price = 15
    discount_percent = 40
    discount_amount = (discount_percent / 100) * CD_price
    total_price = num_cds * CD_price - discount_amount
    sold_price = 40
    total_income = total_price - sold_price
    result = total_income
    return result

print(solution())