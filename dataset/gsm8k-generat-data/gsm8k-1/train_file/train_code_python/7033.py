def solution():
    """Emily goes fishing and has a very busy day. She catches 4 trout, 3 catfish, and 5 bluegills. If the trout weigh 2 pounds each, the catfish weigh 1.5 pounds each, and the bluegills weigh 2.5 pounds each, how many total pounds of fish did she catch?"""
    trout_weight = 2
    catfish_weight = 1.5
    bluegill_weight = 2.5
    num_trout = 4
    num_catfish = 3
    num_bluegill = 5
    total_weight = (trout_weight*num_trout) + (catfish_weight*num_catfish) + (bluegill_weight*num_bluegill)
    result = total_weight
    return result

print(solution())