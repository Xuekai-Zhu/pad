def solution():
    # Calculate the total number of socks knitted by Laticia
    week1_socks = 4 * 2  # knitted 4 pairs of socks
    week2_socks = (12 + 4) * 2  # knitted 4 more pairs than the 12 pairs of the first week
    week3_socks = (week1_socks + week2_socks) / 2  # knitted half of the total of the first two weeks
    week4_socks = (week3_socks - 3) * 2  # knitted 3 fewer pairs than the third week
    total_socks = week1_socks + week2_socks + week3_socks + week4_socks
    result = total_socks
    return result

print(solution())