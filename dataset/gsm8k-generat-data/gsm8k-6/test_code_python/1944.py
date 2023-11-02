def solution():
    # Calculate the total number of cans picked up by LaDonna and Prikya
    cans_picked_up = 25 + 2*25 # Prikya picked up twice as many cans as LaDonna

    # Calculate the number of cans Yoki picked up
    total_cans = 85
    cans_yoki_picked_up = total_cans - cans_picked_up

    result = cans_yoki_picked_up
    return result

print(solution())