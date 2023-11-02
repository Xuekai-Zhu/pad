def solution():
    money = 90
    hat_percent = 60
    scarf_percent = 100 - hat_percent
    hat_cost = (money * hat_percent) / 100
    scarf_cost = (money * scarf_percent) / 100
    hat_amount = hat_cost / 2
    scarf_amount = scarf_cost / 2
    scarf_price = 2
    scarf_number = scarf_amount / scarf_price
    result = scarf_number
    
    return result

print(solution())