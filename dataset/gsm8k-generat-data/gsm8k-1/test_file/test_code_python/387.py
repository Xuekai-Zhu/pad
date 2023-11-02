def solution():
    """The ratio of popsicles that Betty and Sam have is 5:6. If the total number of popsicles they have together is 165, how many more popsicles does Sam have more than Betty?"""
    total_popsicles = 165
    ratio = 5/6
    sam_share = total_popsicles * ratio
    betty_share = total_popsicles - sam_share
    difference = sam_share - betty_share
    result = difference
    return result

print(solution())