def solution():
    
    total_money = 20
    book1_price = 8
    book2_price = 4
    money_left = total_money - book1_price - book2_price
    poster_price = 4
    num_posters = money_left // poster_price
    result = num_posters
    return result

print(solution())