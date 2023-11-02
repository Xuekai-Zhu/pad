def solution():
    """Frank is making hamburgers and he wants to sell them to make $50.  Frank is selling each hamburger for $5 and 2 people purchased 4 and another 2 customers purchased 2 hamburgers.  How many more hamburgers does Frank need to sell to make $50?"""
    # Calculate the number of hamburgers sold so far
    hamburgers_sold = 2*4 + 2*2

    # Calculate the amount of money made so far
    money_made = hamburgers_sold * 5

    # Calculate the number of hamburgers Frank still needs to sell
    hamburgers_needed = (50 - money_made) // 5

    # Display the number of hamburgers Frank still needs to sell
    result = hamburgers_needed
    return result

print(solution())