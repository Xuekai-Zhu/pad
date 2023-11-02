def solution():
    # Calculate the number of questions Lowella got correctly
    lowella_correct = 0.35 * 100

    # Calculate the number of questions Pamela got correctly (20% more than Lowella)
    pamela_correct = lowella_correct * 1.2

    # Calculate the number of questions Mandy got correctly (twice Pamela's score)
    mandy_correct = pamela_correct * 2

    result = mandy_correct
    return result

print(solution())