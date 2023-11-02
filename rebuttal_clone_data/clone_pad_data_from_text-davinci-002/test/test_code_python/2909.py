def solution():
    discount_percent = 50
    Curtis_meal = 16.00
    Rob_meal = 18.00
    Curtis_discount = Curtis_meal * (discount_percent / 100)
    Rob_discount = Rob_meal * (discount_percent / 100)
    total_bill = Curtis_meal - Curtis_discount + Rob_meal - Rob_discount
    result = total_bill
    return result

print(solution())