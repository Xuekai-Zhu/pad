def solution():
    # Calculate the total number of burgers needed
    total_burgers = 15*2 + 15*1  # half the guests want 2 burgers and half want 1

    # Calculate the number of batches Carly needs to cook
    batches = total_burgers/5
    if total_burgers % 5 != 0:
        batches += 1

    # Calculate the total cooking time
    cooking_time = batches*2*4  # each batch takes 2 rounds of 4 minutes on each side

    result = cooking_time
    return result

print(solution())