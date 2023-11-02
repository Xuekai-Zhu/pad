def solution():
    """Ethyl bought Lucy two new dolls for her doll collection. This increased the doll collection by 25%. After the addition of the two new dolls, how many dolls are in Lucy's collection?"""
    # Let x be the original number of dolls in Lucy's collection
    # With the addition of two new dolls, the collection increases by 25%, or 1/4 of the original number of dolls
    # So the equation is x + 2 = x + x/4
    # Solving for x, we get x = 6
    # Therefore, Lucy had 6 dolls in her collection before Ethyl bought her two new ones
    dolls_before = 6

    # The total number of dolls in Lucy's collection after the addition of the two new ones is 6 + 2 = 8
    dolls_after = 8

    # Return the result
    result = dolls_after
    return result

print(solution())