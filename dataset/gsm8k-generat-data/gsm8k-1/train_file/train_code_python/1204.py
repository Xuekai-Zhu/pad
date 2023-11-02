def solution():
    """In a graveyard, there are 20 skeletons. Half of these skeletons are adult women, and the remaining number are split evenly between adult men and children. If an adult woman has 20 bones in their body, and a male has 5 more than this, and a child has half as many as an adult woman, how many bones are in the graveyard?"""
    total_skeletons = 20
    adult_women = total_skeletons / 2
    adult_men_and_children = total_skeletons - adult_women
    adult_men = adult_men_and_children / 2
    children = adult_men_and_children / 2
    adult_women_bones = 20
    adult_men_bones = adult_women_bones + 5
    child_bones = adult_women_bones / 2
    total_bones = (adult_women * adult_women_bones) + (adult_men * adult_men_bones) + (children * child_bones)
    result = total_bones
    return result

print(solution())