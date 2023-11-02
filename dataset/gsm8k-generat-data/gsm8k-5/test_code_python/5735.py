def solution():
    capacity = 2000  # capacity of the stadium is 2000 people
    total_people_3_4_full = capacity * 3/4  # total number of people when stadium is 3/4 full

    # Calculate the fees collected when stadium is 3/4 full
    money_collected_3_4_full = total_people_3_4_full * 20

    # Calculate the fees collected when stadium is full
    money_collected_full = capacity * 20

    # Calculate the difference in fees collected
    difference = money_collected_full - money_collected_3_4_full
    result = difference
    return result

print(solution())