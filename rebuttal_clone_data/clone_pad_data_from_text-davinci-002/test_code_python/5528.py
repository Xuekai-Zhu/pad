def solution():
     male_cattle = 50
     female_cattle = male_cattle * 2
     total_cattle = male_cattle + female_cattle
     male_percent = male_cattle / total_cattle
     female_percent = female_cattle / total_cattle
     milk_produced_by_females = female_cattle * 2
     milk_produced_by_males = milk_produced_by_females * female_percent
     total_milk = milk_produced_by_females + milk_produced_by_males
     result = total_milk
     return result

print(solution())