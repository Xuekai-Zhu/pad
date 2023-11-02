def solution():
    # Calculate the total cost of lattes and croissants for a week
    latte_cost = 3.75
    croissant_cost = 3.50
    total_cost = 7 * (latte_cost + croissant_cost)

    # Calculate the cost of 5 cookies
    cookie_cost = 1.25 * 5

    # Calculate the total cost of all purchases
    total_spending = total_cost + cookie_cost

    # Calculate the remaining balance on the gift card
    gift_card_balance = 100 - total_spending

    result = gift_card_balance
    return result

print(solution())