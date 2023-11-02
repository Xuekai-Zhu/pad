def solution():
    # Define the number of pieces of candy in Sandra's bags
    sandra_bag1 = 6
    sandra_bag2 = 6

    # Define the number of pieces of candy in Roger's bags
    roger_bag1 = 11
    roger_bag2 = 3

    # Calculate the total number of pieces of candy Sandra and Roger have
    sandra_total = sandra_bag1 + sandra_bag2
    roger_total = roger_bag1 + roger_bag2

    # Calculate how much more candy Roger has than Sandra
    candy_difference = roger_total - sandra_total
    result = candy_difference
    return result

print(solution())