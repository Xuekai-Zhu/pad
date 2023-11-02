def solution():
     master_bedroom = 500
     guest_bedroom = 200
     kitchen_and_living_area = 600
     total_house = master_bedroom + guest_bedroom + guest_bedroom + kitchen_and_living_area
     monthly_rent = 3000
     price_per_sq_ft = monthly_rent / total_house
     result = price_per_sq_ft
     return result

print(solution())