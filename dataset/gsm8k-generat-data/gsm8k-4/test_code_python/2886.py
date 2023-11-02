def solution():
    """Samir climbed 318 stairs yesterday. Veronica climbed 18 more than half that amount. How many stairs did Veronica and Samir climb together yesterday?"""
    # Define the number of stairs Samir climbed
    samir_stairs = 318

    # Define the number of stairs Veronica climbed
    veronica_stairs = 0.5 * samir_stairs + 18

    # Calculate the total number of stairs climbed together
    total_stairs = samir_stairs + veronica_stairs

    # return the result
    result = total_stairs
    return result

print(solution())