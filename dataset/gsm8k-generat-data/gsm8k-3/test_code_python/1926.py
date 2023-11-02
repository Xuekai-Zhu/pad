def solution():
    """James buys 10 boxes of Capri-sun.  Each box has 6 pouches in it.  If he paid $12 how many cents does each pouch cost?"""
    # Define the number of boxes and pouches per box
    BOXES = 10
    POUCHES_PER_BOX = 6

    # Calculate the total number of pouches
    total_pouches = BOXES * POUCHES_PER_BOX

    # Calculate the cost per pouch in cents
    cost_per_pouch = (12 * 100) / total_pouches

    result = cost_per_pouch
    return result

print(solution())