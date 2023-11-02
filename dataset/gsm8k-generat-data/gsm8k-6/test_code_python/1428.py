def solution():
    # Calculate the total number of figurines that Adam can make
    basswood_figurines = 15 * 3  # each block of basswood can create 3 figurines
    butternut_figurines = 20 * 4  # each block of butternut wood can create 4 figurines
    aspen_figurines = 20 * 2 * 3  # each block of Aspen wood can make twice the amount of figurines compared to basswood
    total_figurines = basswood_figurines + butternut_figurines + aspen_figurines
    result = total_figurines
    return result

print(solution())