def solution():
    """Robin wants to buy jelly bracelets for her friends. She decides to buy one bracelet for each letter of the first name of her friends. Her friends are Jessica, Tori, Lily and Patrice. If each jelly bracelet costs $2, what is the total she will spend in dollars?"""
    # Define the names of Robin's friends
    friends = ["Jessica", "Tori", "Lily", "Patrice"]

    # Calculate the total number of letters in all of their names
    total_letters = 0
    for friend in friends:
        total_letters += len(friend)

    # Calculate the total cost of buying a bracelet for each letter
    total_cost = total_letters * 2

    # Return the result
    return total_cost

print(solution())