def solution():
    """The big fashion show is being planned for next week. The show includes runway models strutting up and down the runway wearing designer clothing in front of an audience. There are two parts to the show: evening wear and bathing suits. It takes a model 2 minutes to walk out to the end of the runway and back, and models take turns, one at a time, walking the runway up and back, while wearing different clothes. If there are 6 models in the show, and each model will wear two sets of bathing suits and three sets of evening wear clothing during the runway portion of the show, how long will it take, in minutes, to complete all of the runway trips during the show?"""
    num_models = 6
    num_bathing_suit_sets = 2
    num_evening_wear_sets = 3
    time_per_set = 4 # 2 minutes to walk out and back, and models wear two sets
    total_sets = num_models * (num_bathing_suit_sets + num_evening_wear_sets)
    total_time = total_sets * time_per_set
    result = total_time
    return result

print(solution())