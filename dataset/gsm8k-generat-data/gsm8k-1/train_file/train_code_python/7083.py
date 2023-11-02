def solution():
    """Sally is selling boxes of crackers for her scout troop's fund-raiser. If she sells 50% more on Sunday than she sold on Saturday, then she'll have sold a total of 150 boxes on the two days. How many boxes did she sell on Saturday?"""
    total_boxes = 150
    sunday_ratio = 1.5
    saturday_boxes = (total_boxes / (1 + sunday_ratio)) * sunday_ratio
    result = saturday_boxes
    return result

print(solution())