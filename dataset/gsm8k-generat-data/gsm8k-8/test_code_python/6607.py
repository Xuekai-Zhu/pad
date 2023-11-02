def solution():
    # Each dog has 4 nails, so if Carly trimmed 164 nails and 3 dogs had 3 legs, then there were 3*4=12 fewer nails
    total_nails = 164 + 12

    # Each dog with 4 legs has 4 nails, so the number of dogs she worked on is total number of nails divided by 4
    # Note: we assume that all dogs have the same number of nails (4)
    dogs = total_nails / 4
    result = dogs
    return result

print(solution())