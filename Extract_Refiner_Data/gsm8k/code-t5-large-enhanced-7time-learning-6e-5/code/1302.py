def solution():
    
    # Define the number of beakers and Petri dishes gathered
    beakers = 7
    dishes = 14

    # Calculate the number of test tubes and Petri dishes gathered
    test_tubes = 16 / 2
    dishes = dishes + 2

    # Calculate the total number of items gathered
    total_items = test_tubes + beakers + dishes

    # Calculate the number of items Igor lost
    lost_beakers = beakers - beakers

    # Calculate the total number of items gathered
    total_gathered = test_tubes + beakers + dishes

    # Display the total number of items gathered
    result = total_gathered
    return result

print(solution())