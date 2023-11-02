def solution():
    sandra_bag_1 = 6  # Sandra has 6 candies in her first bag
    sandra_bag_2 = 6  # Sandra has 6 candies in her second bag
    roger_bag_1 = 11  # Roger has 11 candies in his first bag
    roger_bag_2 = 3  # Roger has 3 candies in his second bag

    # Calculate the total amount of candy Sandra and Roger have
    sandra_total = sandra_bag_1 + sandra_bag_2
    roger_total = roger_bag_1 + roger_bag_2

    # Calculate how much more candy Roger has than Sandra
    difference = roger_total - sandra_total
    result = difference
    return result

print(solution())