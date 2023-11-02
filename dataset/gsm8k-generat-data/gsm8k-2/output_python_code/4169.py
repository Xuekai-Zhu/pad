def solution():
    """Amon & Rhonda combined have 215 marbles. If Amon owns 55 marbles more than Rhonda, how many marbles does Rhonda have?"""
    combined_marbles = 215
    ar_difference = 55
    # Let R be the number of marbles Rhonda has
    # Then A = R + ar_difference (Amon owns 55 more marbles than Rhonda)
    # And A + R = combined_marbles (combined they have 215 marbles)
    # Substituting A = R + ar_difference into A + R = combined_marbles gives 2R + ar_difference = combined_marbles, which can be solved for R
    rhonda_marbles = (combined_marbles - ar_difference) / 2
    result = rhonda_marbles
    return result

print(solution())