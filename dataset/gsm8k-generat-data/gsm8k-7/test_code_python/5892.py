def solution():
    total_community_members = 2000
    adult_men_percentage = 0.3
    adult_women_multiple = 2

    # Calculate the number of adult men in the event
    num_adult_men = total_community_members * adult_men_percentage

    # Calculate the number of adult women in the event
    num_adult_women = num_adult_men * adult_women_multiple

    # Calculate the number of children in the event
    num_children = total_community_members - num_adult_men - num_adult_women
    result = num_children
    return result

print(solution())