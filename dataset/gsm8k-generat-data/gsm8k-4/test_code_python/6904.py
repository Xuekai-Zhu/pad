def solution():
    """Jonny climbed 1269 stairs last week. Julia climbed 7 less than one-third of that amount. How many stairs did Julia and Jonny climb together?"""
    # Define the number of stairs Jonny climbed
    jonny_stairs = 1269

    # Calculate the number of stairs Julia climbed
    julia_stairs = (jonny_stairs / 3) - 7

    # Calculate the total number of stairs climbed by both
    total_stairs = jonny_stairs + julia_stairs

    # Return the result
    result = total_stairs
    return result

print(solution())