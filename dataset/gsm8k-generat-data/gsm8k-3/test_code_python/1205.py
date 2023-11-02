def solution():
    """In a graveyard, there are 20 skeletons.  Half of these skeletons are adult women, and the remaining number are split evenly between adult men and children.  If an adult woman has 20 bones in their body, and a male has 5 more than this, and a child has half as many as an adult woman, how many bones are in the graveyard?"""
    # Define the number of skeletons and the proportion of each group
    total_skeletons = 20
    women_proportion = 0.5
    men_proportion = 0.25
    children_proportion = 0.25

    # Calculate the number of adult women and their total bones
    women_count = int(total_skeletons * women_proportion)
    women_bones = women_count * 20

    # Calculate the number of adult men and their total bones
    men_count = int(total_skeletons * men_proportion)
    men_bones = men_count * 25

    # Calculate the number of children and their total bones
    children_count = int(total_skeletons * children_proportion)
    children_bones = children_count * 10

    # Calculate the total number of bones in the graveyard
    total_bones = women_bones + men_bones + children_bones

    # Display the total number of bones
    result = total_bones
    return result

print(solution())