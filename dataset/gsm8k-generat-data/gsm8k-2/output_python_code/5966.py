def solution():
    """Laticia knitted 4 pairs of socks for her nephew. She did such a good job that everyone asked her to start selling them. In the first week, she knitted 12 pairs of socks. In the second week, she knitted 4 more pairs than the week before. On the third week, she only knitted half of the total of the first two weeks. In the fourth week, she knitted 3 fewer pairs than the week before. How many pairs of socks did Laticia knit altogether?"""
    initial_pairs = 4
    week1_pairs = 12
    week2_pairs = week1_pairs + 4
    week3_pairs = (week1_pairs + week2_pairs) / 2
    week4_pairs = week3_pairs - 3
    total_pairs = initial_pairs + week1_pairs + week2_pairs + week3_pairs + week4_pairs
    result = total_pairs
    return result

print(solution())