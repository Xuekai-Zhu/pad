def solution():
    """Sandra, the florist around the corner, is very unhappy with Fred's incomplete order delivery. Sandra had ordered four times as many red roses as white carnations. She also ordered 200 pink calla lilies, which were five times the number of white carnations. Sandra has threatened to switch suppliers if the missing red roses are not delivered by 5 pm. To keep Sandra's business, how many red roses must Fred deliver by 5 pm?"""
    white_carnations = 1
    red_roses = 4 * white_carnations
    pink_calla_lilies = 200
    total_carnations = white_carnations + (pink_calla_lilies / 5)
    missing_roses = 4 * total_carnations - red_roses
    result = missing_roses
    return result

print(solution())