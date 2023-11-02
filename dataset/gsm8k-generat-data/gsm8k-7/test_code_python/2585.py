def solution():
    full_price = 85
    years_of_service = 3

    # Calculate the discounted price for officers with at least 1 year of service
    if years_of_service >= 1:
        discount = 0.2
        discounted_price = full_price * (1 - discount)

        # Calculate the additional discount for officers with at least 3 years of service
        if years_of_service >= 3:
            additional_discount = 0.25
            discounted_price *= (1 - additional_discount)

        result = discounted_price
    else:
        result = full_price

    return result

print(solution())