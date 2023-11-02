def solution():
    num_grandchildren = 3

    # Knitting time for each item
    hat_time = 2.0
    scarf_time = 3.0
    mitten_time = 1.0
    sock_time = 1.5
    sweater_time = 6.0

    # Total knitting time for one set of clothes
    total_time = hat_time + scarf_time + 2 * mitten_time + 2 * sock_time + sweater_time

    # Total knitting time for all sets of clothes
    total_time_all_sets = num_grandchildren * total_time
    result = total_time_all_sets
    return result

print(solution())