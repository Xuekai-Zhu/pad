def solution():
    """Will and Henry go fishing in a river. Will catches 16 catfish and 10 eels. Henry challenges himself to catch 3 trout for every catfish Will catches. Due to environmental concerns, Henry decides to return half his catch after meeting his own challenge. How many fishes do they have altogether now?"""
    # Define the number of catfish and eels caught by Will
    will_catfish = 16
    will_eels = 10

    # Calculate the number of trout caught by Henry
    henry_trout = 3 * will_catfish

    # Calculate the total number of fish before Henry returns half
    total_fish = will_catfish + will_eels + henry_trout

    # Calculate the number of fish Henry returns
    returned_fish = 0.5 * henry_trout

    # Calculate the new total number of fish after Henry returns half
    new_total_fish = total_fish - returned_fish

    # Display the new total number of fish
    result = new_total_fish
    return result

print(solution())