def solution():
    """Dr. Hugo Grumpus and his assistant, Igor, were preparing to perform a laboratory experiment. Dr. Grumpus told Igor to gather 16 test tubes, 7 beakers, and 14 Petri dishes, and to place them all on the lab bench. By accident, Igor gathered half as many test tubes as requested, two more than the number of Petri dishes requested. And while he had picked up the correct number of beakers, he lost several on the way to the lab bench. In total, the number of items Igor had placed on the lab bench was 29. How many beakers did Igor lose?"""
    test_tubes_requested = 16
    beakers_requested = 7
    petri_dishes_requested = 14
    test_tubes_gathered = test_tubes_requested / 2
    petri_dishes_gathered = petri_dishes_requested + 2
    beakers_lost = 29 - (test_tubes_gathered + beakers_requested + petri_dishes_gathered)
    result = beakers_lost
    return result

print(solution())