def solution():
     Barbara_stuffed_animals = 9
     Trish_stuffed_animals = Barbara_stuffed_animals * 2
     Barbara_sale_price = 2
     Trish_sale_price = 1.50
     Barbara_total_sale = Barbara_stuffed_animals * Barbara_sale_price
     Trish_total_sale = Trish_stuffed_animals * Trish_sale_price
     total_sale = Barbara_total_sale + Trish_total_sale
     result = total_sale
     return result

print(solution())