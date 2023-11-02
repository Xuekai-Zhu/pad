def solution():
    # Calculate the total number of apples needed for all pies
    total_apples = 1.5 * 8 * 3

    # Calculate the number of apples each guest would eat if they finished all the pie
    apples_per_guest = total_apples / 12

    result = apples_per_guest
    return result

print(solution())