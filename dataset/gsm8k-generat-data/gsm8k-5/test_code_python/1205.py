def solution():
    total_skeletons = 20  # There are 20 skeletons in the graveyard
    adult_women = total_skeletons // 2  # Half of the skeletons are adult women
    adult_men_and_children = (total_skeletons - adult_women) // 2  # The other half is split evenly between adult men and children
    adult_woman_bones = 20  # An adult woman has 20 bones in their body
    adult_man_bones = adult_woman_bones + 5  # A male has 5 more bones than an adult woman
    child_bones = adult_woman_bones / 2  # A child has half as many bones as an adult woman

    # Calculate the total number of bones in the graveyard
    total_bones = (adult_women * adult_woman_bones) + (adult_men_and_children * adult_man_bones) + (adult_men_and_children * child_bones)
    result = total_bones
    return result

print(solution())