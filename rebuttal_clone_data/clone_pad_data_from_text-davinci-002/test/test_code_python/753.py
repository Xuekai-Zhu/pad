def solution():
     amount_before_tax = 150
     sales_tax_rate = 8
     sales_tax_amount = amount_before_tax * (sales_tax_rate / 100)
     total_amount = amount_before_tax + sales_tax_amount
     result = total_amount
     return result

print(solution())