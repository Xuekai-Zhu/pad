def solution():
    """John picks 4 bananas on Wednesday. Then he picks 6 bananas on Thursday. On Friday, he picks triple the number of bananas he did on Wednesday. How many bananas does John have?"""
    wednesday_bananas = 4
    thursday_bananas = 6
    friday_bananas = wednesday_bananas * 3
    total_bananas = wednesday_bananas + thursday_bananas + friday_bananas
    result = total_bananas
    return result

print(solution())