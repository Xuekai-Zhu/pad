def solution():
    """Cynthia harvested 67 potatoes from her garden. After washing them, she cut 13 of them into wedges. She then halved the remaining potatoes and made french fries with one half, and potato chips with the other half. If one potato can be cut into 8 wedges or make 20 potato chips, how many more potato chips than wedges did Cynthia make?"""
    # Define the total number of potatoes harvested
    total_potatoes = 67

    # Calculate the number of potatoes cut into wedges
    wedges_potatoes = 13

    # Calculate the number of potatoes used for French fries
    fries_potatoes = (total_potatoes - wedges_potatoes) / 2

    # Calculate the number of potatoes used for potato chips
    chips_potatoes = (total_potatoes - wedges_potatoes) / 2

    # Calculate the number of chips and wedges from the chips potatoes
    chips = chips_potatoes * 20
    wedges = chips_potatoes * 8

    # Calculate the difference between the number of chips and wedges
    difference = chips - wedges

    # return the result
    result = difference
    return result

print(solution())