def solution():
    total_apples = 85  # Lex picked 85 apples
    wormy_apples = total_apples / 5  # A fifth of the apples have worms
    unbruised_apples = total_apples - wormy_apples  # The remaining apples are unbruised
    bruised_apples = (1/5) * total_apples + 9  # Nine more than one fifth of the apples are bruised

    # Calculate the total number of apples to keep
    total_to_keep = unbruised_apples + bruised_apples

    # Calculate the number of apples left to eat raw
    raw_apples = total_apples - total_to_keep
    result = raw_apples
    return result

print(solution())