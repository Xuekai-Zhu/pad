def solution():
    """Jimmy decides to make sandwiches for a picnic. He makes 8 sandwiches in total, using two slices of bread each. How many packs of bread does he need to buy to make these sandwiches, assuming he starts with no bread and each pack has 4 slices of bread in it?"""
    # Define the number of sandwiches and slices of bread needed
    sandwiches = 8
    slices_needed = sandwiches * 2

    # Calculate the number of bread packs needed
    bread_packs = slices_needed // 4 + (slices_needed % 4 > 0)

    result = bread_packs
    return result

print(solution())