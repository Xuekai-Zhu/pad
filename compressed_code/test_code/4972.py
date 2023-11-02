def solution():
    
    num_olives_needed = 80
    jar_size = 20
    jar_price = 1.5
    num_jars_needed = (num_olives_needed // jar_size) + (num_olives_needed % jar_size > 0)
    total_price = num_jars_needed * jar_price
    change = 10 - total_price
    result = change
    return result

print(solution())