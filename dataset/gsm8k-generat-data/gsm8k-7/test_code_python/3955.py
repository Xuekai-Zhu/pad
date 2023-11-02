def solution():
    sandra_bag1 = 6
    sandra_bag2 = 6
    roger_bag1 = 11
    roger_bag2 = 3

    # Calculate the total number of pieces of candy Sandra had
    sandra_total = sandra_bag1 + sandra_bag2

    # Calculate the total number of pieces of candy Roger had
    roger_total = roger_bag1 + roger_bag2

    # Calculate how much more candy Roger had compared to Sandra
    difference = roger_total - sandra_total
    result = difference
    return result

print(solution())