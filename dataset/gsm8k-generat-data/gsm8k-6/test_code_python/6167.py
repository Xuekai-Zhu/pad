def solution():
    # Find the number of potatoes cut into wedges
    potatoes_wedges = 13  

    # Find the number of potatoes left after cutting into wedges
    potatoes_left = 67 - potatoes_wedges  

    # Find the number of potatoes used for french fries
    potatoes_fries = potatoes_left // 2  

    # Find the number of potatoes used for potato chips
    potatoes_chips = potatoes_left - potatoes_fries  

    # Calculate the difference between the number of potato chips and wedges
    difference = (potatoes_chips * 20) - (potatoes_wedges * 8)  

    result = difference
    return result

print(solution())