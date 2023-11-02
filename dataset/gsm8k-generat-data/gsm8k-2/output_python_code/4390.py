def solution():
    """Libby has 160 quarters in her piggy bank. She has to pay $35 to replace her sister’s dress that she borrowed and ruined. After replacing the dress, how many quarters will Libby have left?"""
    quarters_before = 160
    cost = 35
    quarters_per_dollar = 4    # There are 4 quarters in every dollar
    quarters_spent = cost * quarters_per_dollar
    quarters_after = quarters_before - quarters_spent
    result = quarters_after
    return result

print(solution())