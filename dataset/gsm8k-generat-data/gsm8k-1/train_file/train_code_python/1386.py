def solution():
    """John has 54 pieces of gum, Cole has 45 pieces of gum and Aubrey has no pieces of gum. They decide to share the gum equally between the 3 of them. How many pieces of gum will each one get?"""
    total_gum = 54 + 45 + 0
    num_people = 3
    gum_per_person = total_gum / num_people
    result = gum_per_person
    return result

print(solution())