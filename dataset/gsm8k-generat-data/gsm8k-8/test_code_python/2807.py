def solution():
    # Define the total time it took Osborn to get dressed from Monday to Thursday
    total_time = 2 + 4 + 3 + 4

    # Define the average time it took him from Monday to Thursday
    average_time = total_time / 4

    # Define the time he needs to get dressed on Friday to tie his old method's average time
    friday_time = (5 * average_time) - total_time

    result = friday_time
    return result

print(solution())