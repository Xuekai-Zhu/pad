def solution():
    """The school decided to add 20% to the gym budget. In a normal month, they could buy 15 dodgeballs for $5 each if they spent the entire budget on that. If they only buy softballs instead, which cost $9 each, how many can they buy with the new budget?"""
    original_budget = 15 * 5
    new_budget = 1.2 * original_budget
    softball_price = 9
    num_softballs = new_budget // softball_price
    result = num_softballs
    return result

print(solution())