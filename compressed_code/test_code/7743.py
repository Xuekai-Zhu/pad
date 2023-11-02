def solution():
    
    goods_stolen = 40000
    base_sentence_years = goods_stolen / 5000
    increased_sentence_years = base_sentence_years * 1.25
    total_sentence_years = increased_sentence_years + 2
    result = total_sentence_years
    return result

print(solution())