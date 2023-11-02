def solution():
    # Calculate the number of jeans
    black_shirts = 63
    white_shirts = 42
    sum_shirts = black_shirts + white_shirts
    jeans = round(2/3 * sum_shirts)

    # Calculate the number of scarves
    ties = 34
    belts = 40
    sum_accessories = ties + belts
    scarves = round(1/2 * sum_accessories)

    # Calculate the difference between jeans and scarves
    diff = jeans - scarves
    result = diff
    return result

print(solution())