def solution():
    """Martha's cat catches 3 rats and 7 birds. Cara's cat catches 3 less than five times as many animals as Martha's cat. How many animals does Cara's cat catch?"""
    # Define the number of rats and birds caught by Martha's cat
    martha_rats = 3
    martha_birds = 7

    # Calculate the total number of animals caught by Martha's cat
    martha_total = martha_rats + martha_birds

    # Calculate the number of animals caught by Cara's cat
    cara_total = (5 * martha_total) - 3

    # Display the number of animals caught by Cara's cat
    result = cara_total
    return result

print(solution())