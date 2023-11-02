def solution():
    """John has 10 hectares of a pineapple field. There are 100 pineapples per hectare. John can harvest his pineapples every 3 months. How many pineapples can John harvest within a year?"""
    hectares = 10
    pineapples_per_hectare = 100
    harvests_per_year = 4
    total_pineapples = hectares * pineapples_per_hectare * harvests_per_year
    result = total_pineapples
    return result

print(solution())