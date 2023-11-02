def solution():
    num_oranges = 12  # The boy has 12 oranges
    brother_share = num_oranges / 3  # He gives one-third of the oranges to his brother
    remaining_oranges = num_oranges - brother_share  # Calculate the remaining oranges
    friend_share = remaining_oranges / 4  # He gives one-fourth of the remaining oranges to his friend

    result = friend_share
    return result

print(solution())