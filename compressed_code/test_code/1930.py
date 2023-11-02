def solution():
    
    goods_stolen = 40000
    base_sentence = goods_stolen / 5000
    increased_sentence = base_sentence * 1.25
    additional_sentence = 2
    total_sentence = increased_sentence + additional_sentence
    result = total_sentence
    return result

print(solution())