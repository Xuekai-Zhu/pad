def solution():
    baked_cookies = 5 * 12
    sold_to_teacher = 2 * 12
    sold_to_brock = 7
   sold_to_katy = 2 * sold_to_brock
    total_sold = sold_to_teacher + sold_to_brock + sold_to_katy
    remaining_cookies = baked_cookies - total_sold
    result = remaining_cookies
    return result

print(solution())