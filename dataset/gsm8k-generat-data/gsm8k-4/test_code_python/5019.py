def solution():
    """Sienna gave Bailey half of her suckers. Jen ate half and gave the rest to Molly. Molly ate 2 and gave the rest to Harmony.  Harmony kept 3 and passed the remainder to Taylor. Taylor ate one and gave the last 5 to Callie. How many suckers did Jen eat?"""
    # Define the initial number of suckers
    initial_suckers = None

    # Calculate the number of suckers given to Bailey
    bailey_suckers = initial_suckers / 2

    # Calculate the number of suckers eaten by Jen
    jen_suckers = bailey_suckers / 2

    # Calculate the number of suckers given to Molly
    molly_suckers = bailey_suckers - jen_suckers

    # Calculate the number of suckers eaten by Harmony
    harmony_suckers = molly_suckers - 2

    # Calculate the number of suckers passed to Taylor
    taylor_suckers = harmony_suckers

    # Calculate the number of suckers eaten by Taylor
    taylor_eaten = 1

    # Calculate the number of suckers passed to Callie
    callie_suckers = taylor_suckers - taylor_eaten - 5

    # Calculate the number of suckers eaten by Jen
    jen_eaten = initial_suckers / 2 - jen_suckers - molly_suckers - harmony_suckers - taylor_suckers - taylor_eaten - callie_suckers

    # return the result
    result = jen_eaten
    return result

print(solution())