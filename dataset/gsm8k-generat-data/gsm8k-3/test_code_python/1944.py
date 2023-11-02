def solution():
    """Eighty-five cans were collected. LaDonna picked up 25 cans. Prikya picked up twice as many times as many cans as LaDonna. Yoki picked up the rest of the cans. How many cans did Yoki pick up?"""
    # Define the number of cans LaDonna picked up
    ladonna_cans = 25

    # Calculate the number of cans Prikya picked up
    prikya_cans = ladonna_cans * 2

    # Calculate the total number of cans collected by LaDonna and Prikya
    total_cans = ladonna_cans + prikya_cans

    # Calculate the number of cans Yoki picked up
    yoki_cans = 85 - total_cans

    # Display the number of cans Yoki picked up
    result = yoki_cans
    return result

print(solution())