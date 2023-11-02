def solution():
    """The big fashion show is being planned for next week. The show includes runway models strutting up and down the runway wearing designer clothing in front of an audience. There are two parts to the show: evening wear and bathing suits. It takes a model 2 minutes to walk out to the end of the runway and back, and models take turns, one at a time, walking the runway up and back, while wearing different clothes. If there are 6 models in the show, and each model will wear two sets of bathing suits and three sets of evening wear clothing during the runway portion of the show, how long will it take, in minutes, to complete all of the runway trips during the show?"""
    # Define the number of models and the number of clothing sets they will wear
    num_models = 6
    num_bathing_suits = 2
    num_evening_wear = 3

    # Calculate the total number of trips each model will take on the runway
    total_trips_per_model = num_bathing_suits + num_evening_wear

    # Calculate the total number of trips for all models combined
    total_trips = total_trips_per_model * num_models

    # Calculate the total time it will take for all trips
    total_time = total_trips * 2

    # Return the result
    result = total_time
    return result

print(solution())