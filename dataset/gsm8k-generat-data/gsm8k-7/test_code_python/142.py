def solution():
    spray1_effectiveness = 0.5
    spray2_effectiveness = 0.25
    shared_effectiveness = 0.05

    # Calculate the combined effectiveness of both sprays
    combined_effectiveness = spray1_effectiveness + spray2_effectiveness - (spray1_effectiveness * spray2_effectiveness * shared_effectiveness)

    # Calculate the percentage of germs that would be left after using both sprays together
    percent_left = (1 - combined_effectiveness) * 100
    result = percent_left
    return result

print(solution())