def solution():
    """Alexis has four times as many mangoes as Dilan and Ashley combined. If Alexis has 60 mangoes, how many mangoes does all of them have combined?"""
    alexis_mangoes = 60
    dilan_ashley_mangoes = alexis_mangoes / 4
    total_mangoes = alexis_mangoes + dilan_ashley_mangoes * 2
    result = total_mangoes
    return result

print(solution())