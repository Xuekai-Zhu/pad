def solution():
    """Nick hides 10 chocolates in his closet. His brother Alix hides 3 times as many chocolates than Nick hides. Last night, their mom found and took 5 chocolates from Alix. How many more chocolates does Alix have than Nick?"""
    # Define the number of chocolates Nick hides
    nick_chocolates = 10

    # Define the number of chocolates Alix hides
    alix_chocolates = 3 * nick_chocolates

    # Calculate the number of chocolates Alix has after their mom takes 5
    alix_chocolates -= 5

    # Calculate the difference in the number of chocolates that Alix has compared to Nick
    difference = alix_chocolates - nick_chocolates

    # Display the difference
    result = difference
    return result

print(solution())