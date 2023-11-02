def solution():
    """Sara’s house is 100 square feet larger than 2 times Nada's house. If Sara's house is 1000 square feet, how many square feet is Nada's house?"""
    sara_house = 1000
    sara_house_size = sara_house - 100
    nada_house_size = (sara_house_size / 2)
    result = nada_house_size
    return result

print(solution())