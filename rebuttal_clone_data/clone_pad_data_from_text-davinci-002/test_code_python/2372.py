def solution():
    price_adult_buffet = 30
    price_children_buffet = 15
    discount_senior_citizens = 10
    number_adults = 2
    number_children = 3
    number_senior_citizens = 2
    total_price = (number_adults * price_adult_buffet) + (number_children * price_children_buffet) + ((number_senior_citizens * price_adult_buffet) * (discount_senior_citizens / 100))
    result = total_price
    return result

print(solution())