def solution():
     total_champions = 25
     percent_women = 60
     percent_men = 40
     percent_bearded_men = 40
     num_women = total_champions * (percent_women / 100)
     num_men = total_champions * (percent_men / 100)
     num_bearded_men = num_men * (percent_bearded_men / 100)
     result = num_bearded_men
     return result

print(solution())