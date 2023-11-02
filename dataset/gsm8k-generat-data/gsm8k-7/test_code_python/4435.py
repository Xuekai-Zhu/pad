def solution():
    total_spent = 25
    milk_price = 3
    cereal_price = 3.5
    bananas_price = 0.25
    apples_price = 0.5

    # Calculate the total cost of all items except cookies
    total_without_cookies = milk_price + (2 * cereal_price) + (4 * bananas_price) + (4 * apples_price)

    # Calculate the cost of cookies
    cookies_price = total_spent - total_without_cookies

    # Calculate the cost of one box of cookies
    milk_price_double = milk_price * 2
    cookies_per_box = cookies_price / milk_price_double

    result = cookies_per_box
    return result

print(solution())