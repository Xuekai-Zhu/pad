def solution():
    """Libby has 160 quarters in her piggy bank. She has to pay $35 to replace her sister’s dress that she borrowed and ruined. After replacing the dress, how many quarters will Libby have left?"""
    quarters = 160
    cost = 35
    quarters_left = quarters - (cost / 0.25)
    result = quarters_left
    return result

print(solution())