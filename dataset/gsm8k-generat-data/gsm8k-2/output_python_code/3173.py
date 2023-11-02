def solution():
    """There were 30 women and 20 men who attended the party. After few hours, 2/5 of the total number of people left. If 9 men left the party, how many more women stayed at the party than men?"""
    initial_women = 30
    initial_men = 20
    total_people = initial_women + initial_men
    left_percentage = 2/5
    left_total = left_percentage * total_people
    left_men = 9
    left_women = left_total - left_men
    remained_women = initial_women - left_women
    remained_men = initial_men - left_men
    women_more_than_men = abs(remained_women - remained_men)
    result = women_more_than_men
    return result

print(solution())