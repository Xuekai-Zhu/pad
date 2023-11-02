def solution():
    starting_candies = 100
    num_siblings = 3
    candies_per_sibling = 10
    candies_given_to_siblings = num_siblings * candies_per_sibling

    # Calculate the number of candies Josh has left after giving some to his siblings
    candies_left_after_siblings = starting_candies - candies_given_to_siblings

    # Calculate the number of candies Josh gives to his friend
    candies_given_to_friend = candies_left_after_siblings / 2

    # Calculate the total number of candies left for Josh and others to share
    total_candies_left = candies_left_after_siblings - candies_given_to_friend - 16
    result = total_candies_left
    return result

print(solution())