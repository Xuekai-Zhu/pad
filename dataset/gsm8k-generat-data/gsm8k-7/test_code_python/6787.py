def solution():
    koby_boxes = 2
    koby_sparklers_per_box = 3
    koby_whistlers_per_box = 5

    cherie_boxes = 1
    cherie_sparklers_per_box = 8
    cherie_whistlers_per_box = 9

    # Calculate the total number of sparklers that Koby has
    total_koby_sparklers = koby_boxes * koby_sparklers_per_box

    # Calculate the total number of whistlers that Koby has
    total_koby_whistlers = koby_boxes * koby_whistlers_per_box

    # Calculate the total number of sparklers that Cherie has
    total_cherie_sparklers = cherie_boxes * cherie_sparklers_per_box

    # Calculate the total number of whistlers that Cherie has
    total_cherie_whistlers = cherie_boxes * cherie_whistlers_per_box

    # Calculate the total number of fireworks that Koby and Cherie have
    total_fireworks = (total_koby_sparklers + total_koby_whistlers + total_cherie_sparklers + total_cherie_whistlers)

    result = total_fireworks
    return result

print(solution())