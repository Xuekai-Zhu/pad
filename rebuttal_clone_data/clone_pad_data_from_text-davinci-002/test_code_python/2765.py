def solution():
     people_ordering_ice_cream = 220
     percent_ordering_vanilla = 20
     people_ordering_vanilla = people_ordering_ice_cream * (percent_ordering_vanilla / 100)
     people_ordering_chocolate = people_ordering_ice_cream - people_ordering_vanilla
     result = people_ordering_chocolate
     
     return result

print(solution())