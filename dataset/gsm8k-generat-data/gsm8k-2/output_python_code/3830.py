def solution():
    """Jerry bought 48 firecrackers for the 4th of July. A police officer discovered and confiscated 12 of them. 1/6 of the remaining ones were defective. If Jerry set off half the good firecrackers, how many firecrackers did he set off?"""
    total_firecrackers = 48
    confiscated_firecrackers = 12
    remaining_firecrackers = total_firecrackers - confiscated_firecrackers
    defective_firecrackers = remaining_firecrackers / 6
    good_firecrackers = remaining_firecrackers - defective_firecrackers
    set_off_firecrackers = good_firecrackers / 2
    result = set_off_firecrackers
    return result

print(solution())