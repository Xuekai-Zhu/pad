def solution():
     total_bill = 140
     sales_tax = 10
     food_charge = 80
     drink_charge = 10
     tip_percentage = 20
     tax_percentage = sales_tax + tip_percentage
     total_tax = (total_bill * tax_percentage) / 100
     gratuity_charge = (total_bill + total_tax - food_charge - drink_charge)
     result = gratuity_charge
     return result

print(solution())