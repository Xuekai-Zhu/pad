def solution():
    """At a gathering, it was reported that 26 people took wine, 22 people took soda, and 17 people took both drinks. If each person could have taken one or more drinks regardless of what was reported, how many people altogether were at the gathering?"""
    # Use the formula for finding the size of the union of two sets
    # size(union(A,B)) = size(A) + size(B) - size(intersection(A,B))
    # Let A be the set of people who took wine and B be the set of people who took soda
    size_union = 26 + 22 - 17

    # The total number of people who took either wine or soda is the size of the union
    # Therefore, the total number of people who attended the gathering is at least the size of the union
    # However, some people may have taken drinks other than wine or soda, so the actual number may be larger
    # Therefore, we know that the number of people who attended the gathering is at least 31
    result = 31
    return result

print(solution())