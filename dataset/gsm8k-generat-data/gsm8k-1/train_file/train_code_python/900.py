def solution():
    """Sandi had $600. She spent half of it at a farmer’s market. Gillian spent $150 more than three times Sandi's total. What is the total that Gillian spent at the farmer’s market?"""
    sandi_spent = 600 / 2
    gillian_spent = 3 * sandi_spent + 150
    result = gillian_spent
    
    return result

print(solution())