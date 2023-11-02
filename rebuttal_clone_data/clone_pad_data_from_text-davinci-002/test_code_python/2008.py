def solution():
     percent_oysters_with_pearls = 25
     oysters_per_dive = 16
     desired_pearls = 56
     oysters_needed = desired_pearls / percent_oysters_with_pearls
     dives_needed = oysters_needed / oysters_per_dive
     result = dives_needed
     return result

print(solution())