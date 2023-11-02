def solution():
    # Define the initial number of suckers Sienna had
    initial = 2 * (Jen + Molly + Harmony + Taylor + Callie + 2 + 3 + 5 + 1)

    # Calculate the number of suckers that Bailey got
    bailey = initial / 2

    # Calculate the number of suckers that Jen got
    jen = bailey / 2

    # Calculate the number of suckers that Molly got
    molly = bailey - jen

    # Calculate the number of suckers that Harmony got
    harmony = molly / 2 - 2

    # Calculate the number of suckers that Taylor got
    taylor = harmony - 3

    # Calculate the number of suckers that Callie got
    callie = 5

    # Calculate the total number of suckers
    total = bailey + jen + molly + harmony + taylor + callie

    # Calculate the number of suckers that Jen ate
    jen_ate = jen / 2

    result = jen_ate
    return result

print(solution())