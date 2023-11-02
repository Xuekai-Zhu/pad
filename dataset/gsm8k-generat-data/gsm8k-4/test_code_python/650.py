def solution():
    """Josh had 100 gummy bear candies. He decided to give his 3 siblings 10 candies each. Then he gave half of the remaining candies to his best friend. If he only wants to eat 16 gummy bear candies, how many candies are left to be shared with others?"""
    # Define the initial number of candies
    candies_initial = 100

    # Define the number of candies given to each sibling
    candies_sibling = 10

    # Calculate the number of candies given to all siblings
    candies_given_siblings = candies_sibling * 3

    # Calculate the remaining number of candies after giving to the siblings
    candies_remaining = candies_initial - candies_given_siblings

    # Calculate the number of candies given to the best friend
    candies_given_friend = candies_remaining / 2

    # Calculate the number of candies left after Josh ate some
    candies_left = candies_given_friend - 16

    # return the result
    result = candies_left
    return result

print(solution())