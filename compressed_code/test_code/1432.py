def solution():
    
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