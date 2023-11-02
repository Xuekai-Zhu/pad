def solution():
    """Ittymangnark and Kingnook are an Eskimo couple living in the most northern region of the Alaskan wilderness. Together, they live with their child, Oomyapeck. Every day Ittymangnark catches enough fish for the three of them to eat for the day and they split the fish equally between the three of them. But after they have split the fish, they give Oomyapeck all of the eyes, who gives two of the eyes to his dog and eats the rest himself. How many fish will each of them be given to eat if Oomyapeck eats 22 eyes in a day?"""
    total_eyes = 22
    oomyapeck_eyes = total_eyes - 2
    total_fish = oomyapeck_eyes / 2
    fish_per_person = total_fish / 3
    result = fish_per_person
    return result

print(solution())