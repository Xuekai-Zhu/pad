def solution():
    total_cans = 85
    ladonna_cans = 25
    prikya_cans = ladonna_cans * 2

    # Calculate the total number of cans picked up by Ladonna and Prikya
    total_picked_up = ladonna_cans + prikya_cans

    # Calculate the number of cans picked up by Yoki
    yoki_cans = total_cans - total_picked_up
    result = yoki_cans
    return result

print(solution())