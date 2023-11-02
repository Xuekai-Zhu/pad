def solution():
 
bill = 5000
percent_for_medication = 50
percent_for_overnight_stay = 25
amount_for_food = 175

medication_cost = bill * (percent_for_medication / 100)
overnight_stay_cost = (bill - medication_cost) * (percent_for_overnight_stay / 100)
 ambulance_cost = bill - medication_cost - overnight_stay_cost - amount_for_food
 
result = ambulance_cost

return result

print(solution())