def solution():
    """The big fashion show is being planned for next week.  The show includes runway models strutting up and down the runway wearing designer clothing in front of an audience.  There are two parts to the show: evening wear and bathing suits.  It takes a model 2 minutes to walk out to the end of the runway and back, and models take turns, one at a time, walking the runway up and back, while wearing different clothes.  If there are 6 models in the show, and each model will wear two sets of bathing suits and three sets of evening wear clothing during the runway portion of the show, how long will it take, in minutes, to complete all of the runway trips during the show?"""
    # Define the number of models and the time it takes for each model to complete a runway trip
    NUM_MODELS = 6
    RUNWAY_TRIP_TIME = 2

    # Define the number of different clothing sets each model will wear
    BATHING_SUITS = 2
    EVENING_WEAR = 3

    # Calculate the total number of runway trips needed for all models
    total_trips = NUM_MODELS * (BATHING_SUITS + EVENING_WEAR)

    # Calculate the total time needed for all runway trips
    total_time = total_trips * RUNWAY_TRIP_TIME

    # Display the total time needed for all runway trips
    result = total_time
    return result

print(solution())