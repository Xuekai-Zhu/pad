def solution():
    """Donna made a cake to take to a party where the guests ate half the cake. The day after the party, she shared half the leftovers with her brothers. The following day, she ate one piece as a midnight snack. Twice as many pieces as her snack were left. How many pieces was the cake to begin with?"""
    # At the party, half of the cake was eaten
    remaining_cake = 0.5

    # The day after the party, half of the leftover cake was shared with brothers
    remaining_cake *= 0.5

    # The following day, Donna ate one piece as a midnight snack
    remaining_cake -= 1

    # Twice as many pieces as her snack were left
    remaining_cake *= 2

    # The original cake was the sum of the remaining cake and the pieces eaten
    original_cake = remaining_cake + 1

    # Display the number of pieces the cake had to begin with
    result = original_cake
    return result

print(solution())