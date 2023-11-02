def solution():
    t_shirt_price = 8
    sweater_price = 18
    jacket_price = 80
    discount = 10
    sales_tax = 5
    number_of_t_shirts = 6
    number_of_sweaters = 4
    number_of_jackets = 5
    cost_of_t_shirts = t_shirt_price * number_of_t_shirts
    cost_of_sweaters = sweater_price * number_of_sweaters
    cost_of_jackets = jacket_price * number_of_jackets * (1 - (discount/100))
    pre_tax_total = cost_of_t_shirts + cost_of_sweaters + cost_of_jackets
    tax = pre_tax_total * (sales_tax/100)
    total_cost = pre_tax_total + tax
    result = total_cost
    
    return result

print(solution())