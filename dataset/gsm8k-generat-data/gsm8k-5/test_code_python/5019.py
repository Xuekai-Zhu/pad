def solution():
    # Sienna gave half of her suckers to Bailey
    sienna_suckers = x
    bailey_suckers = sienna_suckers / 2

    # Jen ate half of Bailey's suckers
    jen_suckers = bailey_suckers / 2

    # Molly ate some of Jen's suckers
    molly_suckers = jen_suckers / 2 - 2

    # Harmony kept some of Molly's suckers
    harmony_suckers = molly_suckers - 3

    # Taylor ate some of Harmony's suckers
    taylor_suckers = harmony_suckers - 1

    # Callie ate the rest of Taylor's suckers
    callie_suckers = 5

    # Calculate how many suckers Jen ate
    jen_suckers = bailey_suckers / 2 - molly_suckers - harmony_suckers - taylor_suckers - callie_suckers
    result = jen_suckers
    return result

print(solution())