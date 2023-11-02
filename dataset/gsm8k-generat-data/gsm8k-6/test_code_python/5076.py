def solution():
    # Calculate the new selling price of the TV after the price increase
    tv_price = 500
    tv_increase = 2/5
    tv_new_price = tv_price + tv_price * tv_increase

    # Calculate the new selling price of the phone after the price increase
    phone_price = 400
    phone_increase = 40/100
    phone_new_price = phone_price + phone_price * phone_increase

    # Calculate the total amount received for both items after the auction
    total_amount = tv_new_price + phone_new_price
    result = total_amount
    return result

print(solution())