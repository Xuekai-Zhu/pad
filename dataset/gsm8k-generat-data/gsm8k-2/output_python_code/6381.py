def solution():
    """A case of water contains 24 bottles. A children's camp comprising of 4 groups purchased 13 cases for a 3-day camp.
    The first group has 14 children, the second group has 16 children, the third group has 12 children, and the fourth group
    has half of the number of the first three groups combined. If each child consumes 3 bottles a day, how many more bottles
    of water does the camp organizer still need to buy?"""
    
    num_cases = 13
    num_children_group1 = 14
    num_children_group2 = 16
    num_children_group3 = 12
    num_children_group4 = (num_children_group1 + num_children_group2 + num_children_group3) / 2
    num_bottles_per_child_per_day = 3
    num_days = 3
    
    num_bottles_needed = (num_children_group1 + num_children_group2 + num_children_group3 + num_children_group4) * num_bottles_per_child_per_day * num_days
    num_bottles_available = num_cases * 24
    
    num_bottles_to_buy = num_bottles_needed - num_bottles_available
    
    result = num_bottles_to_buy
    return result

print(solution())