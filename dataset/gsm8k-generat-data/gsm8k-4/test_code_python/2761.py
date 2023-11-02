def solution():
    """Will catches 16 catfish and 10 eels. Henry challenges himself to catch 3 trout for every catfish Will catches. Due to environmental concerns, Henry decides to return half his catch after meeting his own challenge. How many fishes do they have altogether now?"""
    # Define the number of catfish and eels caught by Will
    catfish_will = 16
    eels_will = 10

    # Calculate the number of trout caught by Henry
    trout_henry = catfish_will * 3

    # Calculate the total number of fish before Henry returns half of his catch
    total_fish_before = catfish_will + eels_will + trout_henry

    # Calculate the number of fish Henry returns
    trout_returned = trout_henry / 2

    # Calculate the total number of fish after Henry returns half of his catch
    total_fish_after = catfish_will + eels_will + trout_henry - trout_returned

    # Return the result
    result = total_fish_after
    return result

print(solution())