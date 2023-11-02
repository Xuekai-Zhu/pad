def solution():
    """Laticia knitted 4 pairs of socks for her nephew. She did such a good job that everyone asked her to start selling them. In the first week, she knitted 12 pairs of socks. In the second week, she knitted 4 more pairs than the week before. On the third week, she only knitted half of the total of the first two weeks. In the fourth week, she knitted 3 fewer pairs than the week before. How many pairs of socks did Laticia knit altogether?"""
    # Define the number of pairs of socks knitted each week
    week1 = 12
    week2 = week1 + 4
    week3 = (week1 + week2) / 2
    week4 = week3 - 3

    # Calculate the total number of pairs of socks knitted
    total = 4 + week1 + week2 + week3 + week4

    # Display the total number of pairs of socks knitted
    result = total
    return result

print(solution())