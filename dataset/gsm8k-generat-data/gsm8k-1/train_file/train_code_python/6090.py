def solution():
    """A store puts out a product sample every Saturday. The last Saturday, the sample product came in boxes of 20. If they had to open 12 boxes, and they had five samples left over at the end of the day, how many customers tried a sample if the samples were limited to one per person?"""
    boxes_opened = 12
    samples_per_box = 20
    samples_leftover = 5
    total_samples = boxes_opened * samples_per_box - samples_leftover
    result = total_samples
    return result

print(solution())