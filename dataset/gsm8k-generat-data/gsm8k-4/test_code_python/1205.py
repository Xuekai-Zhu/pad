def solution():
    """In a graveyard, there are 20 skeletons. Half of these skeletons are adult women, and the remaining number are split evenly between adult men and children. If an adult woman has 20 bones in their body, and a male has 5 more than this, and a child has half as many as an adult woman, how many bones are in the graveyard?"""
    # Define the number of skeletons in the graveyard
    total_skeletons = 20

    # Calculate the number of adult women
    adult_women = total_skeletons // 2

    # Calculate the number of remaining skeletons
    remaining_skeletons = total_skeletons - adult_women

    # Calculate the number of adult men
    adult_men = remaining_skeletons // 2

    # Calculate the number of children
    children = remaining_skeletons - adult_men

    # Calculate the total number of bones
    total_bones = (adult_women * 20) + (adult_men * 25) + (children * 10)

    # return the result
    result = total_bones
    return result

print(solution())