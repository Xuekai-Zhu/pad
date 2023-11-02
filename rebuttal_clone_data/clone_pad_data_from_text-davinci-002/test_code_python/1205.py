def solution():
     adult_women = 20
     adult_men = adult_women / 2
     children = adult_women / 2
     bones_per_adult_woman = 20
     bones_per_adult_man = bones_per_adult_woman + 5
     bones_per_child = bones_per_adult_woman / 2
     total_bones = (adult_women * bones_per_adult_woman) + (adult_men * bones_per_adult_man) + (children * bones_per_child)
     result = total_bones
     return result

print(solution())