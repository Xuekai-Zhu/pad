def solution():
    """Joanna and Jacques had 40 and 60 gumballs, respectively, in their dishes. They then purchased 4 times the number of gumballs they had initially and added these to their dishes. If they decided to put together their gumballs and shared them equally, how many gumballs did each get?"""
    joanna_initial = 40
    jacques_initial = 60
    purchased = 4 * (joanna_initial + jacques_initial)
    total = joanna_initial + jacques_initial + purchased
    each_get = total / 2
    result = each_get
    return result

print(solution())