def solution():
    location = "United States"
    currency_used = "United States dollar"
    payment_currency = "Euros"
    if location == "United States" and payment_currency != currency_used:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())