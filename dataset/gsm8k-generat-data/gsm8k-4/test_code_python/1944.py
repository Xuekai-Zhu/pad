def solution():
    """Eighty-five cans were collected. LaDonna picked up 25 cans. Prikya picked up twice as many times as many cans as LaDonna. Yoki picked up the rest of the cans. How many cans did Yoki pick up?"""
    # Define the total number of cans and LaDonna's cans
    total_cans = 85
    ladonna_cans = 25

    # Calculate the number of cans Prikya picked up and the remaining cans for Yoki
    prikya_cans = 2 * ladonna_cans
    yoki_cans = total_cans - ladonna_cans - prikya_cans

    # return the result
    result = yoki_cans
    return result

print(solution())