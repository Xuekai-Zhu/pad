def solution():
    """Samir climbed 318 stairs yesterday. Veronica climbed 18 more than half that amount. How many stairs did Veronica and Samir climb together yesterday?"""
    # Define the number of stairs Samir climbed
    samir_stairs = 318

    # Calculate the number of stairs Veronica climbed
    veronica_stairs = 18 + 0.5 * samir_stairs

    # Calculate the total number of stairs climbed
    total_stairs = samir_stairs + veronica_stairs

    # Display the total number of stairs climbed
    result = total_stairs
    return result

print(solution())