def solution():
    """Rebecca bought 2 pies for the holiday weekend. Each pie was sliced into 8 slices. Rebecca ate 1 slice of each pie. Her family and friends ate 50% of the remaining pies over the weekend. On Sunday evening Rebecca and her husband each had another slice of pie. How many slices are remaining?"""
    pies = 2
    slices_per_pie = 8
    rebecca_slices = 2
    remaining_slices = (pies * slices_per_pie) - rebecca_slices
    remaining_slices *= 0.5
    remaining_slices -= 2
    result = remaining_slices
    return result

print(solution())