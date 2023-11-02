def solution():
    """A basic manicure starts at $35 while a pedicure starts at $40. A certain salon offers 20% off if you get both. Suppose Karen chooses to do both and would also like to add nail art on each of her fingers, which costs $3 per nail. How much would she pay in all?"""
    basic_manicure_cost = 35
    pedicure_cost = 40
    discount_percent = 20
    nail_art_cost = 3 * 10  # 10 nails in total for both hands
    basic_and_pedicure_cost = basic_manicure_cost + pedicure_cost
    discount_amount = basic_and_pedicure_cost * (discount_percent / 100)
    total_cost_before_tax = basic_and_pedicure_cost + nail_art_cost - discount_amount
    sales_tax_percent = 8.25
    sales_tax_amount = total_cost_before_tax * (sales_tax_percent / 100)
    total_cost = total_cost_before_tax + sales_tax_amount
    result = total_cost
    return result

print(solution())