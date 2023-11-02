def solution():
    """Josh had 100 gummy bear candies. He decided to give his 3 siblings 10 candies each. Then he gave half of the remaining candies to his best friend. If he only wants to eat 16 gummy bear candies, how many candies are left to be shared with others?"""
    # Define the number of gummy bear candies Josh starts with
    starting_candies = 100

    # Define the number of candies given to each sibling
    sibling_candies = 10
    num_siblings = 3

    # Calculate the number of candies Josh has left after giving to his siblings
    candies_left = starting_candies - (sibling_candies * num_siblings)

    # Calculate the number of candies Josh gives to his best friend
    candies_given = candies_left / 2

    # Calculate the number of candies Josh has left after giving to his friend
    candies_left -= candies_given

    # Calculate the final number of candies after Josh eats 16
    candies_left -= 16

    # Display the number of candies left to be shared
    result = candies_left
    return result

print(solution())