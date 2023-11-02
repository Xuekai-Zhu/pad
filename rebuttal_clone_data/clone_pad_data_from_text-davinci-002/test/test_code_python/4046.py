def solution():
     seashells_picked_monday = 30
     seashells_picked_tuesday = seashells_picked_monday / 2
     total_seashells = seashells_picked_monday + seashells_picked_tuesday
     price_per_seashell = 1.20
     total_revenue = total_seashells * price_per_seashell
     result = total_revenue
     return result

print(solution())