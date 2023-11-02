def solution():
    """There are many CDs in the store. The rock and roll CDs are $5 each, the pop CDs are $10 each, the dance CDs are $3 each, and the country CDs are $7 each. Julia wants to buy 4 of each, but she only has 75 dollars. How much money is she short?"""
    rock_price = 5
    pop_price = 10
    dance_price = 3
    country_price = 7
    num_of_cds = 4
    total_price = (rock_price + pop_price + dance_price + country_price) * num_of_cds
    difference = total_price - 75
    result = difference
    return result

print(solution())