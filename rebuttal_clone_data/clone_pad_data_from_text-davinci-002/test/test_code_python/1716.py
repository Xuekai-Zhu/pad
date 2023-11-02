def solution():
     kg_harvested_wed = 400
     kg_harvested_thu = kg_harvested_wed / 2
     kg_harvested_fri = 2000 - kg_harvested_wed - kg_harvested_thu
     kg_given_away = 700
     kg_remaining = kg_harvested_fri - kg_given_away
     result = kg_remaining
     return result

print(solution())