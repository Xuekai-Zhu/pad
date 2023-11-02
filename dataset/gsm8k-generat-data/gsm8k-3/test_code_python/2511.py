def solution():
    """James decides to use tannerite to blow things up to reveal his baby's gender. The explosion ignites both his neighbors' houses and attracts a police officer, who arrests James on two count of arson, one count of manufacturing explosives, and one count of domestic terrorism. If the arson counts each carry a 6-year sentence, the explosives sentence is twice as long as the total arson sentence, and the domestic terrorism charge's sentence is 20 years, how long might James spend in jail?"""
    # Define the length of the arson sentence
    ARSON_SENTENCE = 6

    # Calculate the length of the explosives sentence
    explosives_sentence = ARSON_SENTENCE * 2

    # Calculate the total length of the arson sentences
    total_arson_sentence = ARSON_SENTENCE * 2

    # Calculate the total length of James' sentence
    total_sentence = total_arson_sentence + explosives_sentence + 20

    # Display the total length of James' sentence
    result = total_sentence
    return result

print(solution())