def solution():
    """Robin wants to buy jelly bracelets for her friends. She decides to buy one bracelet for each letter of the first name of her friends. Her friends are Jessica, Tori, Lily and Patrice. If each jelly bracelet costs $2, what is the total she will spend in dollars?"""
    # Define the number of letters in each friend's name
    jessica = 7
    tori = 4
    lily = 4
    patrice = 7

    # Calculate the total number of bracelets needed
    total_bracelets = jessica + tori + lily + patrice

    # Calculate the total cost of the bracelets
    total_cost = total_bracelets * 2

    # Display the total cost
    result = total_cost
    return result

print(solution())