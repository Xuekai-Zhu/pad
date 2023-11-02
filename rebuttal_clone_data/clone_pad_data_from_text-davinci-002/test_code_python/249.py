def solution():
     """Caleb picked a handful of dandelion puffs. He gave 3 to his mom, another 3 to his sister, 5 to his grandmother, and 2 to his dog. Then, he divided the remaining dandelion puffs equally among his 3 friends. How many dandelion puffs did each friend receive if he originally picked 40 dandelion puffs?"""
     dandelion_puffs = 40
     puffs_given_away = 3 + 3 + 5 + 2
     puffs_left = dandelion_puffs - puffs_given_away
     puffs_per_friend = puffs_left / 3
     result = puffs_per_friend
     return result

print(solution())