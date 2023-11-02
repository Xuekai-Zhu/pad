def solution():
    bill_before_discount_bob = 30
    discount_percentage_bob = 5
    bill_before_discount_kate = 25
    discount_percentage_kate = 2
    bill_after_discount_bob = bill_before_discount_bob - (bill_before_discount_bob * (discount_percentage_bob / 100))
    bill_after_discount_kate = bill_before_discount_kate - (bill_before_discount_kate * (discount_percentage_kate / 100))
    result = bill_after_discount_bob + bill_after_discount_kate
    
    return result

print(solution())