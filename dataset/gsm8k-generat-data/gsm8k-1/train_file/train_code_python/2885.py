def solution():
    """Samir climbed 318 stairs yesterday. Veronica climbed 18 more than half that amount. How many stairs did Veronica and Samir climb together yesterday?"""
    samir_stairs = 318
    veronica_stairs = (0.5 * samir_stairs) + 18
    total_stairs = samir_stairs + veronica_stairs
    result = total_stairs
    return result

print(solution())