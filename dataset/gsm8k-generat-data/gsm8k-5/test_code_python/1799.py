def solution():
    guitar_price = 1000  # The price of the guitar is $1000
    gc_discount = 0.15  # Guitar Center offers a 15% discount
    gc_shipping_fee = 100  # Guitar Center has a $100 shipping fee
    sw_discount = 0.1  # Sweetwater offers a 10% discount
    sw_shipping_fee = 0  # Sweetwater has free shipping

    # Calculate the total cost of the guitar from Guitar Center
    gc_total_cost = guitar_price - (guitar_price * gc_discount) + gc_shipping_fee

    # Calculate the total cost of the guitar from Sweetwater
    sw_total_cost = guitar_price - (guitar_price * sw_discount) + sw_shipping_fee

    # Calculate the amount Silvia will save by buying from Sweetwater compared to Guitar Center
    savings = gc_total_cost - sw_total_cost
    result = savings
    return result

print(solution())