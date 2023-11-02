def solution():
    """One batch of cookies requires 4 cups of flour and 1.5 cups of sugar. How many cups of flour and sugar combined would be needed for 8 batches?"""
    flour_per_batch = 4
    sugar_per_batch = 1.5
    total_flour = flour_per_batch * 8
    total_sugar = sugar_per_batch * 8
    total_combined = total_flour + total_sugar
    result = total_combined
    return result

print(solution())