def solution():
    """Adam bought himself some new trousers for $30. His mother gave him $6 for this purpose, and his father gave him twice as much. How much money did Adam have to contribute from his savings?"""
    total_cost = 30
    amount_given_by_mother = 6
    amount_given_by_father = 2 * amount_given_by_mother
    amount_contributed_by_adam = total_cost - amount_given_by_mother - amount_given_by_father
    result = amount_contributed_by_adam
    return result

print(solution())