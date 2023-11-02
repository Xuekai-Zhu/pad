def solution():
    """In a field of 500 clovers, 20% have four leaves and one quarter of these are purple clovers. Assuming these proportions are exactly correct, how many clovers in the field are both purple and four-leaved?"""
    # Define the total number of clovers in the field
    TOTAL_CLOVERS = 500

    # Calculate the number of four-leaved clovers
    four_leaved_clovers = int(TOTAL_CLOVERS * 0.2)

    # Calculate the number of purple clovers among the four-leaved clovers
    purple_clovers = int(four_leaved_clovers * 0.25)

    # Display the number of clovers that are both purple and four-leaved
    result = purple_clovers
    return result

print(solution())