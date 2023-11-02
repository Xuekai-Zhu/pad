def solution():
    chocolate_cookies = 220  # You sold 220 chocolate cookies
    vanilla_cookies = 70  # You sold 70 vanilla cookies
    price_chocolate = 1  # Each chocolate cookie was sold for $1
    price_vanilla = 2  # Each vanilla cookie was sold for $2

    # Calculate the total revenue from chocolate cookies
    revenue_chocolate = chocolate_cookies * price_chocolate

    # Calculate the total revenue from vanilla cookies
    revenue_vanilla = vanilla_cookies * price_vanilla

    # Calculate the total revenue from all cookies
    total_revenue = revenue_chocolate + revenue_vanilla
    result = total_revenue
    return result

print(solution())