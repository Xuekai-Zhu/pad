def solution():
    brothers_in_first_half = 3  # 3 brothers with birthdays in March
    brothers_in_second_half = 4  # 1 brother with a birthday in October, 1 brother in November, and 2 brothers in December
    presents_per_brother = 2  # buy each brother a birthday present and a Christmas present

    # Calculate the total number of presents Santana has to buy in the first half of the year
    presents_in_first_half = brothers_in_first_half * presents_per_brother

    # Calculate the total number of presents Santana has to buy in the second half of the year
    presents_in_second_half = brothers_in_second_half * presents_per_brother

    # Calculate the difference in the number of presents between the two halves of the year
    presents_difference = presents_in_second_half - presents_in_first_half
    result = presents_difference
    return result

print(solution())