def solution():
     pint_of_paint = 8.00
     gallon_of_paint = 55.00
     pints_needed = 8
     cost_of_pints = pints_needed * pint_of_paint
     cost_of_gallon = gallon_of_paint
     money_saved = cost_of_pints - cost_of_gallon
     result = money_saved
     return result

print(solution())