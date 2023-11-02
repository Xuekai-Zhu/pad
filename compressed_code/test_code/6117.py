def solution():
    
    shoes_sold = 6
    shoe_price = 3
    shirts_sold = 18
    shirt_price = 2
    total_sales = (shoes_sold * shoe_price) + (shirts_sold * shirt_price)
    earnings_per_person = total_sales / 2
    result = earnings_per_person
    return result

print(solution())