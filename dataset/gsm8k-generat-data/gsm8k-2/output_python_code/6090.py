def solution():
    """A store puts out a product sample every Saturday. The last Saturday, the sample product came in boxes of 20. If they had to open 12 boxes, and they had five samples left over at the end of the day, how many customers tried a sample if the samples were limited to one per person?"""
    box_size = 20
    num_boxes = 12
    total_samples = box_size * num_boxes
    leftover_samples = 5
    num_customers = total_samples - leftover_samples
    result = num_customers
    return result

print(solution())