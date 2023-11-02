def solution():
    initial_count = 300
    leaving_rate = 28
    leaving_time = 4
    arriving_rate = 15
    arriving_time = 7

    # Calculate the number of athletes leaving the camp on Saturday morning
    leaving_count = leaving_rate * leaving_time

    # Calculate the number of athletes arriving at the camp on Sunday morning
    arriving_count = arriving_rate * arriving_time

    # Calculate the total number of athletes in the camp on Sunday morning
    total_count = initial_count - leaving_count + arriving_count

    # Calculate the difference in the total number of athletes between the two nights
    difference = total_count - initial_count
    result = difference
    return result

print(solution())