def solution():
    # Calculate the number of pairs of socks knitted in each week
    week1 = 12
    week2 = week1 + 4
    week3 = (week1 + week2) / 2
    week4 = week3 - 3

    # Calculate the total number of pairs of socks knitted
    total = 4 + week1 + week2 + week3 + week4

    result = total
    return result

print(solution())