def solution():
    # Calculate Annie's number of toys using Mike's number as a reference
    annie_to_mike_ratio = 3
    annie_to_mike_difference = annie_to_mike_ratio - 1
    annie_toys = (annie_to_mike_ratio * 6) + annie_to_mike_difference

    # Calculate Tom's number of toys using Annie's number as a reference
    tom_to_annie_ratio = 1.5
    tom_to_annie_difference = 2
    tom_toys = (tom_to_annie_ratio * annie_toys) - tom_to_annie_difference

    # Calculate the total number of toys
    total_toys = annie_toys + mike_toys + tom_toys
    result = total_toys
    return result

print(solution())