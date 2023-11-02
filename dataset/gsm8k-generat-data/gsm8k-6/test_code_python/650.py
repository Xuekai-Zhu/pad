def solution():
    # Calculate the number of candies that Josh gives to his siblings
    candy_given_to_siblings = 3 * 10  # each of his 3 siblings gets 10 candies

    # Calculate the number of candies left after giving to his siblings
    candies_left = 100 - candy_given_to_siblings

    # Calculate the number of candies that Josh gives to his best friend
    candy_given_to_best_friend = candies_left / 2

    # Calculate the number of candies left after giving to his best friend
    candies_left_after_best_friend = candies_left - candy_given_to_best_friend

    # Calculate the number of candies left after Josh eats 16 of them
    candies_left_after_eating = candies_left_after_best_friend - 16

    result = candies_left_after_eating
    return result

print(solution())