def solution():
    # Calculate the total number of marbles Miriam gave away
    total_given_away = 60 + 2*60 + 3*30  # Miriam gave her brother 60 marbles, her sister 2*60 marbles, and her friend Savanna 3 times the amount she currently has

    # Calculate the number of marbles Miriam started with
    started_with = total_given_away + 30  # Miriam currently has 30 marbles

    result = started_with
    return result

print(solution())