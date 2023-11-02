def solution():
    # Define the number of each item in the store
    num_ties = 34
    num_belts = 40
    num_black_shirts = 63
    num_white_shirts = 42

    # Calculate the number of jeans and scarfs
    num_jeans = (2/3) * (num_black_shirts + num_white_shirts)
    num_scarves = 0.5 * (num_ties + num_belts)

    # Calculate the difference between the number of jeans and scarfs
    difference = num_jeans - num_scarves
    result = difference
    return result

print(solution())