def solution():
    # Calculate the total number of tins of beans
    total_tins = 15 * 24  # 15 cases of tins of beans, each case contains 24 tins

    # Calculate the number of tins that are damaged and thrown away
    damaged_tins = total_tins * 0.05  # 5% of the tins are damaged and thrown away

    # Calculate the number of tins of beans that are left
    remaining_tins = total_tins - damaged_tins
    result = remaining_tins
    return result

print(solution())