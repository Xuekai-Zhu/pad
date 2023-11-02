def solution():
    """A store puts out a product sample every Saturday. The last Saturday, the sample product came in boxes of 20. If they had to open 12 boxes, and they had five samples left over at the end of the day, how many customers tried a sample if the samples were limited to one per person?"""
    # Define the number of boxes opened and samples left over
    boxes_opened = 12
    samples_left = 5

    # Calculate the total number of samples available
    total_samples = (boxes_opened * 20) + samples_left

    # Determine the number of customers who tried a sample
    customers_tried = total_samples - samples_left

    # Display the number of customers who tried a sample
    result = customers_tried
    return result

print(solution())