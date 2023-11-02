def solution():
    """Betty and Dora started making some cupcakes at the same time. Betty makes 10 cupcakes every hour and Dora makes 8 every hour. If Betty took a two-hour break, what is the difference between the number of cupcakes they made after 5 hours?"""
    # Define the number of cupcakes each person can make per hour
    BETTY_RATE = 10
    DORA_RATE = 8

    # Calculate the number of cupcakes each person made before Betty's break
    betty_cupcakes1 = BETTY_RATE * 3
    dora_cupcakes1 = DORA_RATE * 3

    # Calculate the number of cupcakes each person made after Betty's break
    betty_cupcakes2 = BETTY_RATE * 2
    dora_cupcakes2 = DORA_RATE * 5

    # Calculate the total number of cupcakes each person made
    betty_total = betty_cupcakes1 + betty_cupcakes2
    dora_total = dora_cupcakes1 + dora_cupcakes2

    # Calculate the difference in the number of cupcakes each person made
    difference = abs(betty_total - dora_total)

    # Display the difference in the number of cupcakes each person made
    result = difference
    return result

print(solution())