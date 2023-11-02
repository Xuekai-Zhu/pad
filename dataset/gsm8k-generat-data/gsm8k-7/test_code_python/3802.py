def solution():
    gift_card_amount = 100
    num_lattes = 7
    latte_price = 3.75
    num_croissants = 7
    croissant_price = 3.5
    num_cookies = 5
    cookie_price = 1.25

    # Calculate the total cost of lattes
    total_latte_cost = num_lattes * latte_price

    # Calculate the total cost of croissants
    total_croissant_cost = num_croissants * croissant_price

    # Calculate the total cost of cookies
    total_cookie_cost = num_cookies * cookie_price

    # Calculate the total cost of all items
    total_cost = total_latte_cost + total_croissant_cost + total_cookie_cost

    # Calculate the remaining balance on the gift card
    remaining_balance = gift_card_amount - total_cost
    result = remaining_balance
    return result

print(solution())