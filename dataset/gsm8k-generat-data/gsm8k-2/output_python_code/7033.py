def solution():
    """Emily goes fishing and has a very busy day. She catches 4 trout, 3 catfish, and 5 bluegills. If the trout weigh 2 pounds each, the catfish weigh 1.5 pounds each, and the bluegills weigh 2.5 pounds each, how many total pounds of fish did she catch?"""
    trout_weight = 2
    catfish_weight = 1.5
    bluegill_weight = 2.5
    total_trout_weight = 4 * trout_weight
    total_catfish_weight = 3 * catfish_weight
    total_bluegill_weight = 5 * bluegill_weight
    total_weight = total_trout_weight + total_catfish_weight + total_bluegill_weight
    result = total_weight
    return result

print(solution())