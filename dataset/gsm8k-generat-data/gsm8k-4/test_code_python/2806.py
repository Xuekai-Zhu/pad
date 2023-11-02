def solution():
    """John buys 4 pounds of beef. He uses all but 1 pound in soup. He uses twice as many pounds of vegetables as beef. How many pounds of vegetables did he use?"""
    # Define the initial amount of beef
    beef = 4

    # Calculate the amount of beef used in the soup
    beef_used = beef - 1

    # Calculate the amount of vegetables used, which is twice the amount of beef used
    vegetables_used = beef_used * 2

    # return the result
    result = vegetables_used
    return result

print(solution())