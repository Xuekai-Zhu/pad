def solution():
    """The big fashion show is being planned for next week. The show includes runway models strutting up and down the runway wearing designer clothing in front of an audience. There are two parts to the show: evening wear and bathing suits. It takes a model 2 minutes to walk out to the end of the runway and back, and models take turns, one at a time, walking the runway up and back, while wearing different clothes. If there are 6 models in the show, and each model will wear two sets of bathing suits and three sets of evening wear clothing during the runway portion of the show, how long will it take, in minutes, to complete all of the runway trips during the show?"""
    num_models = 6
    sets_of_bathing_suits = 2
    sets_of_evening_wear = 3
    runway_trip_time = 2
    total_runs_per_model = sets_of_bathing_suits + sets_of_evening_wear
    total_runs = total_runs_per_model * num_models
    total_runway_time = total_runs * runway_trip_time
    result = total_runway_time
    return result

print(solution())