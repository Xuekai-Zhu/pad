def solution():
    # Find the total number of situps Shawna has to do
    total_situps = 30
    # Find the number of situps Shawna has already done
    done_situps = 12 + 19  # situps done on Monday and Tuesday
    # Find the number of situps Shawna has to do on Wednesday
    remaining_situps = total_situps - done_situps
    result = remaining_situps
    return result

print(solution())