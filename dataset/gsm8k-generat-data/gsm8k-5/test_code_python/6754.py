def solution():
    # Let's call the number of pictures that Quincy drew "q"
    # Then we know that Peter drew 8 pictures and Quincy drew 20 more than that, so
    q = 8 + 20

    # We also know that altogether they drew 41 pictures, so we can set up an equation to solve for Randy's number of pictures
    # Randy's number of pictures + Peter's number of pictures + Quincy's number of pictures = 41
    # Randy's number of pictures + 8 + (8 + 20) = 41
    # Randy's number of pictures = 41 - 8 - (8 + 20) = 5

    # So Randy drew 5 pictures in total
    result = 5
    return result

print(solution())