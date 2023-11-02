def solution():
    """A fixer uses 30% of the nails in a container to repair the kitchen. He also used 70% of the remaining nails in the container to repair the fence. If there were 400 nails in the container, how many nails are remaining?"""
    # Define the number of nails in the container
    nails_total = 400

    # Calculate the number of nails used in the kitchen
    nails_kitchen = int(nails_total * 0.3)

    # Calculate the number of nails remaining after the kitchen repair
    nails_remaining1 = nails_total - nails_kitchen

    # Calculate the number of nails used in the fence repair
    nails_fence = int(nails_remaining1 * 0.7)

    # Calculate the number of nails remaining after the fence repair
    nails_remaining2 = nails_remaining1 - nails_fence

    # Display the number of nails remaining
    result = nails_remaining2
    return result

print(solution())