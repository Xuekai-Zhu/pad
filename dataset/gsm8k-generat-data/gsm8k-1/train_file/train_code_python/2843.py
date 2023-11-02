def solution():
    """Ethyl bought Lucy two new dolls for her doll collection. This increased the doll collection by 25%. After the addition of the two new dolls, how many dolls are in Lucy's collection?"""
    percent_increase = 25
    increase_amount = 2 * (percent_increase / 100)
    initial_amount = (2 / (1 + increase_amount)) * 100
    total_dolls = initial_amount + 2
    result = total_dolls
    return result

print(solution())