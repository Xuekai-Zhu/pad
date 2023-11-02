def solution():
    # Calculate the total liters of water drank on Mon, Thurs, and Sat
    total_liters_1 = 9 + 9 + 9

    # Calculate the total liters of water drank on Tues, Fri, and Sun
    total_liters_2 = 8 + 8 + 8

    # Calculate the total liters of water drank for the whole week
    total_liters = 60

    # Calculate the liters of water drank on Wednesday
    liters_on_wed = total_liters - total_liters_1 - total_liters_2

    result = liters_on_wed
    return result

print(solution())