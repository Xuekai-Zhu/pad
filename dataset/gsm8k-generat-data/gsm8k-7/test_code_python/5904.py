def solution():
    total_spots = 59

    # Let x be the number of spots Phil has
    # Bill has one less than twice as many spots as Phil
    # So, Bill has (2x - 1) spots
    x = (total_spots + 1) / 3
    bill_spots = 2*x - 1

    result = bill_spots
    return result

print(solution())