def solution():
    """Carson leans over the railing at the zoo to get the perfect selfie and falls into the combined wombat and rhea enclosure.  There are 9 wombats and 3 rheas. If each wombat claws him 4 times and each rhea claws him once, how many times does he get clawed?"""
    # Define the number of wombats and rheas
    NUM_WOMBATS = 9
    NUM_RHEAS = 3

    # Define the number of times Carson is clawed by each wombat and rhea
    WOMBAT_CLAWS = 4
    RHEA_CLAWS = 1

    # Calculate the total number of times Carson is clawed
    total_claws = NUM_WOMBATS * WOMBAT_CLAWS + NUM_RHEAS * RHEA_CLAWS

    # Display the total number of claws Carson receives
    result = total_claws
    return result

print(solution())