def solution():
    basswood_figurines_per_block = 3
    butternut_figurines_per_block = 4
    aspen_figurines_per_block = 6  # twice the amount of basswood

    # Calculate the total number of figurines Adam can make with each type of wood
    total_basswood_figurines = basswood_figurines_per_block * 15
    total_butternut_figurines = butternut_figurines_per_block * 20
    total_aspen_figurines = aspen_figurines_per_block * 20

    # Calculate the total number of figurines Adam can make with all the wood
    total_figurines = total_basswood_figurines + total_butternut_figurines + total_aspen_figurines
    result = total_figurines
    return result

print(solution())