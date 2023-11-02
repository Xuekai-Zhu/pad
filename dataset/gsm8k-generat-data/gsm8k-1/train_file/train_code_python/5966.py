def solution():
    """Laticia knitted 4 pairs of socks for her nephew. She did such a good job that everyone asked her to start selling them. In the first week, she knitted 12 pairs of socks. In the second week, she knitted 4 more pairs than the week before. On the third week, she only knitted half of the total of the first two weeks. In the fourth week, she knitted 3 fewer pairs than the week before. How many pairs of socks did Laticia knit altogether?"""
    first_week = 12
    second_week = first_week + 4
    third_week = (first_week + second_week) / 2
    fourth_week = third_week - 3
    total_socks = (4 * 2 * first_week) + (second_week * 2) + (third_week * 2) + (fourth_week * 2)
    result = total_socks
    return result

print(solution())