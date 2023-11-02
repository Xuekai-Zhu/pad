def solution():
    house_price = 500000  # James sold a $500,000 house
    market_value = house_price / 1.2  # James sold the house for 20% over market value, so market value is 80% of the selling price
    revenue = house_price - market_value  # James made a revenue of 20% over market value
    share_per_person = revenue / 4  # James has 3 brothers, so the revenue is split between 4 people
    taxed_share = share_per_person * 0.9  # 10% tax is taken away from each person's share

    result = taxed_share
    return result

print(solution())