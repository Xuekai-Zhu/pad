def solution():
    """Alexis has four times as many mangoes as Dilan and Ashley combined. If Alexis has 60 mangoes, how many mangoes does all of them have combined?"""
    # Define the number of mangoes Alexis has and the ratio of mangoes between them
    alexis_mangoes = 60
    ratio = 4

    # Calculate the total number of mangoes
    total_mangoes = alexis_mangoes / (ratio + 1) * (ratio + 2)

    result = total_mangoes
    return result

print(solution())