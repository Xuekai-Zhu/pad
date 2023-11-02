def solution():
    """Adam owns a wood carving shop, if a block of basswood can create 3 figurines and a block of butternut wood can create 4 figurines, and a block of Aspen wood can make twice the amount of figurines compared to basswood, how many figurines can he make if he owns 15 blocks of basswood, 20 blocks of butternut wood, and 20 blocks of Aspen wood?"""
    basswood_figurines = 3
    butternut_figurines = 4
    aspen_figurines = 2 * basswood_figurines
    
    total_basswood_figurines = basswood_figurines * 15
    total_butternut_figurines = butternut_figurines * 20
    total_aspen_figurines = aspen_figurines * 20
    
    total_figurines = total_basswood_figurines + total_butternut_figurines + total_aspen_figurines
    
    result = total_figurines
    return result

print(solution())