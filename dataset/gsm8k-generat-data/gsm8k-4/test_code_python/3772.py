def solution():
    """The running time of Beast of War: Armoured Command is 10 minutes longer than that of Alpha Epsilon, which is 30 minutes shorter than that of Millennium. If Millennium runs for 2 hours, what is the running time of Beast of War: Armoured Command in minutes?"""
    # Define the running time of Millennium in minutes
    millennium_time = 2 * 60

    # Calculate the running time of Alpha Epsilon in minutes
    ae_time = millennium_time - 30

    # Calculate the running time of Beast of War: Armoured Command in minutes
    boc_time = ae_time + 10

    # return the result
    result = boc_time
    return result

print(solution())