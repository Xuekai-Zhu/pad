def solution():
    powerpuff_girls_names = ["Blossom", "Buttercup", "Bubbles"]
    initial_consonant_sound = powerpuff_girls_names[0][0].lower() # get the first letter of the first name and convert to lowercase
    alliterative = True
    for name in powerpuff_girls_names:
        if name[0].lower() != initial_consonant_sound:
            alliterative = False
            break
    if alliterative:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())