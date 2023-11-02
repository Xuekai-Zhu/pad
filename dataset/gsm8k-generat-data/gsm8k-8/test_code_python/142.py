def solution():
    #Calculate the percentage of germs left after using the first spray
    first_spray = 50
    germs_left_after_first_spray = 100 - first_spray

    #Calculate the percentage of germs left after using the second spray
    second_spray = 25
    germs_left_after_second_spray = 100 - second_spray

    #Calculate the percentage of germs left after using both sprays
    germs_left_after_both_sprays = germs_left_after_first_spray * (germs_left_after_second_spray/100)

    # Subtract the percentage of germs killed by both sprays from 100 to get the percentage of germs left
    germs_left_percentage = 100 - germs_left_after_both_sprays - 5
    result = germs_left_percentage
    return result

print(solution())