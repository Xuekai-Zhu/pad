def solution():
    """Frank picked 36 apples. Susan picked 3 times as many apples as Frank. If Susan gave out half of her apples, and Frank sold a third of his, how many in total do they have left?"""
    frank_apples = 36
    susan_apples = 3 * frank_apples
    susan_gave_away = susan_apples / 2
    frank_sold = frank_apples / 3
    total_left = frank_apples + susan_apples - susan_gave_away - frank_sold
    result = total_left
    return result

print(solution())