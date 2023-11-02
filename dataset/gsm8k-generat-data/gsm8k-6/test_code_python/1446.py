def solution():
    # Calculate the number of jeans and scarves in the store
    black_shirts = 63
    white_shirts = 42
    jeans = (2/3) * (black_shirts + white_shirts)
    ties = 34
    belts = 40
    scarves = (1/2) * (ties + belts)

    # Calculate the difference between jeans and scarves
    difference = jeans - scarves
    result = difference
    return result

print(solution())