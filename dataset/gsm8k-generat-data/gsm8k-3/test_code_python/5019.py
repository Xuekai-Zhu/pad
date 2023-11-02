def solution():
    """Sienna gave Bailey half of her suckers. Jen ate half and gave the rest to Molly. Molly ate 2 and gave the rest to Harmony. Harmony kept 3 and passed the remainder to Taylor. Taylor ate one and gave the last 5 to Callie. How many suckers did Jen eat?"""
    # Define the total number of suckers originally had by Sienna
    sienna_suckers = 0

    # Calculate the total number of suckers after each transfer
    bailey_suckers = sienna_suckers / 2
    jen_suckers = bailey_suckers / 2
    molly_suckers = jen_suckers
    harmony_suckers = molly_suckers - 2
    taylor_suckers = harmony_suckers
    callie_suckers = taylor_suckers - 6

    # Calculate the number of suckers Jen ate
    jen_suckers_eaten = jen_suckers - molly_suckers

    # Display the number of suckers Jen ate
    result = jen_suckers_eaten
    return result

print(solution())