def solution():
    """Dawn, Lydia, and Donna have a total of 200 bananas. Dawn has 40 more bananas than Lydia. If Lydia has 60 bananas, how many bananas does Donna have?"""
    lydia_bananas = 60
    dawn_bananas = lydia_bananas + 40
    total_bananas = 200
    donna_bananas = total_bananas - lydia_bananas - dawn_bananas
    result = donna_bananas
    return result

print(solution())