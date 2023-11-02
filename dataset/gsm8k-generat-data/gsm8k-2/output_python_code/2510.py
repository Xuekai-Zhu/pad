def solution():
    """James decides to use tannerite to blow things up to reveal his baby's gender. The explosion ignites both his neighbors' houses and attracts a police officer, who arrests James on two count of arson, one count of manufacturing explosives, and one count of domestic terrorism. If the arson counts each carry a 6-year sentence, the explosives sentence is twice as long as the total arson sentence, and the domestic terrorism charge's sentence is 20 years, how long might James spend in jail?"""
    arson_sentence = 6
    total_arson_sentence = 2 * arson_sentence
    explosives_sentence = 2 * total_arson_sentence
    domestic_terrorism_sentence = 20
    total_sentence = total_arson_sentence + explosives_sentence + domestic_terrorism_sentence
    result = total_sentence
    return result

print(solution())