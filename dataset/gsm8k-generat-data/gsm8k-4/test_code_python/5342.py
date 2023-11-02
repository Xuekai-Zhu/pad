def solution():
    """Nick hides 10 chocolates in his closet. His brother Alix hides 3 times as many chocolates than Nick hides. Last night, their mom found and took 5 chocolates from Alix. How many more chocolates does Alix have than Nick?"""
    # Define the number of chocolates Nick hides
    nick_chocolates = 10

    # Calculate the number of chocolates Alix hides
    alix_chocolates = nick_chocolates * 3

    # Subtract the number of chocolates that their mom took from Alix's chocolates
    alix_chocolates -= 5

    # Calculate the difference between the number of Alix's and Nick's chocolates
    difference = alix_chocolates - nick_chocolates

    # return the result
    result = difference
    return result

print(solution())