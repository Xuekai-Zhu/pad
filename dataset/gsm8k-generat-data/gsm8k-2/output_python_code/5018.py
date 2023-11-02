def solution():
    """Sienna gave Bailey half of her suckers. Jen ate half and gave the rest to Molly. Molly ate 2 and gave the rest to Harmony. Harmony kept 3 and passed the remainder to Taylor. Taylor ate one and gave the last 5 to Callie. How many suckers did Jen eat?"""
    sienna_suckers = 2*x
    bailey_suckers = sienna_suckers / 2
    jen_suckers = bailey_suckers / 2
    molly_suckers = jen_suckers
    molly_suckers -= 2
    harmony_suckers = molly_suckers
    harmony_suckers -= 3
    taylor_suckers = harmony_suckers
    taylor_suckers -= 1
    callie_suckers = taylor_suckers
    callie_suckers -= 5
    result = jen_suckers
    return result

print(solution())