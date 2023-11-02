def solution():
    """Cynthia harvested 67 potatoes from her garden. After washing them, she cut 13 of them into wedges. She then halved the remaining potatoes and made french fries with one half, and potato chips with the other half. If one potato can be cut into 8 wedges or make 20 potato chips, how many more potato chips than wedges did Cynthia make?"""
    # Define the number of potatoes harvested and the number of potatoes cut into wedges
    potatoes_harvested = 67
    potatoes_wedges = 13

    # Calculate the number of potatoes used for french fries and potato chips
    potatoes_remaining = potatoes_harvested - potatoes_wedges
    potatoes_halved = potatoes_remaining / 2

    # Calculate the number of potato chips and wedges
    potato_chips = potatoes_halved * 20
    potato_wedges = potatoes_wedges * 8

    # Calculate the difference between the number of potato chips and wedges
    difference = potato_chips - potato_wedges

    # Display the difference
    result = difference
    return result

print(solution())