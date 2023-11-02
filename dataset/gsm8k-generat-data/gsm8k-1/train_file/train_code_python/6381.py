def solution():
    """A case of water contains 24 bottles. A children's camp comprising of 4 groups purchased 13 cases for a 3-day camp. The first group has 14 children, the second group has 16 children, the third group has 12 children, and the fourth group has half of the number of the first three groups combined. If each child consumes 3 bottles a day, how many more bottles of water does the camp organizer still need to buy?"""
    bottles_per_case = 24
    num_cases_purchased = 13
    num_days = 3
    group1_children = 14
    group2_children = 16
    group3_children = 12
    group4_children = (group1_children + group2_children + group3_children) / 2
    total_children = group1_children + group2_children + group3_children + group4_children
    total_bottles_needed = total_children * num_days * 3
    total_bottles_purchased = bottles_per_case * num_cases_purchased
    bottles_remaining = total_bottles_purchased - total_bottles_needed
    result = max(0, bottles_remaining)
    return result

print(solution())