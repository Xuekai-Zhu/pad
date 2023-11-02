def solution():
    
    total_skeletons = 20
    adult_women_count = total_skeletons // 2
    adult_men_and_children_count = total_skeletons - adult_women_count
    adult_women_bones = 20
    adult_men_bones = 20 + 5
    child_bones = 20 // 2
    total_bones = (adult_women_count * adult_women_bones) + (adult_men_and_children_count//2 * (adult_men_bones + child_bones))
    result = total_bones
    return result

print(solution())