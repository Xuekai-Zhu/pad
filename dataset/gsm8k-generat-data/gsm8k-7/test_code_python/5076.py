def solution():
    tv_initial_price = 500
    tv_price_increase = 2/5
    phone_initial_price = 400
    phone_price_increase = 40/100

    # Calculate the final price of the TV
    tv_final_price = tv_initial_price + (tv_initial_price * tv_price_increase)

    # Calculate the final price of the phone
    phone_final_price = phone_initial_price + (phone_initial_price * phone_price_increase)

    # Calculate the total amount Bethany received from selling both items
    total_amount = tv_final_price + phone_final_price
    result = total_amount
    return result

print(solution())