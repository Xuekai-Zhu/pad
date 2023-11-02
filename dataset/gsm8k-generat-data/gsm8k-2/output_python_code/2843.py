def solution():
    """Ethyl bought Lucy two new dolls for her doll collection. This increased the doll collection by 25%. After the addition of the two new dolls, how many dolls are in Lucy's collection?"""
    percent_increase = 0.25
    new_dolls = 2
    total_dolls = int((new_dolls / percent_increase) * 100)
    result = total_dolls
    return result

print(solution())