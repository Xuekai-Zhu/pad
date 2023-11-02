def solution():
    
    total_brownies = 10 * 20
    for_sale_brownies = total_brownies * 3 / 4
    remaining_brownies = total_brownies - for_sale_brownies
    container_brownies = remaining_brownies * 3 / 5
    given_out_brownies = remaining_brownies - container_brownies
    result = given_out_brownies
    return result

print(solution())