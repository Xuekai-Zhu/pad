def solution():
    
    total_time = 120  
    baking_time = 15
    white_icing_time = 30
    chocolate_icing_time = 30
    dough_and_cool_time = total_time - (baking_time + white_icing_time + chocolate_icing_time)
    result = dough_and_cool_time
    return result

print(solution())