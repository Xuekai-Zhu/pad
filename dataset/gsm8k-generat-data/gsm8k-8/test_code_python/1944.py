def solution():
    # Define the number of cans picked up by LaDonna and Prikya
    ladonna_cans = 25
    prikya_cans = ladonna_cans * 2

    # Calculate the total number of cans picked up by all three
    total_cans = ladonna_cans + prikya_cans + 85 - ladonna_cans - prikya_cans

    # Calculate the number of cans picked up by Yoki
    yoki_cans = total_cans
    result = yoki_cans
    return result

print(solution())