def solution():
    total_firecrackers = 48  # Jerry bought 48 firecrackers
    confiscated_firecrackers = 12  # A police officer discovered and confiscated 12 of them
    remaining_firecrackers = total_firecrackers - confiscated_firecrackers  # Jerry has the remaining firecrackers
    defective_firecrackers = remaining_firecrackers / 6  # 1/6 of the remaining firecrackers were defective
    good_firecrackers = remaining_firecrackers - defective_firecrackers  # Jerry has the number of good firecrackers
    set_off_firecrackers = good_firecrackers / 2  # Jerry set off half of the good firecrackers

    result = set_off_firecrackers
    return result

print(solution())