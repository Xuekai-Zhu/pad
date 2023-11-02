def solution():
    """James decides to use tannerite to blow things up to reveal his baby's gender. The explosion ignites both his neighbors' houses and attracts a police officer, who arrests James on two count of arson, one count of manufacturing explosives, and one count of domestic terrorism. If the arson counts each carry a 6-year sentence, the explosives sentence is twice as long as the total arson sentence, and the domestic terrorism charge's sentence is 20 years, how long might James spend in jail?"""
    # Define the sentence length for each charge
    arson_sentence = 6
    explosives_sentence = 2 * arson_sentence
    terrorism_sentence = 20

    # Calculate the total sentence length
    total_sentence = (arson_sentence * 2) + explosives_sentence + terrorism_sentence

    # Return the result
    return total_sentence

print(solution())