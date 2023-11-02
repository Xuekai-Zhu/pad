def solution():
     potatoes_harvested = 67
     potatoes_cut_into_wedges = 13
     potatoes_cut_into_fries = (potatoes_harvested - potatoes_cut_into_wedges) / 2
     potatoes_cut_into_chips = potatoes_cut_into_fries
     wedges_per_potato = 8
     chips_per_potato = 20
     total_wedges = potatoes_cut_into_wedges * wedges_per_potato
     total_chips = potatoes_cut_into_chips * chips_per_potato
     difference = total_chips - total_wedges
     result = difference
     return result
 

Question: A truck can drive 550 miles on a tank of gas. If gas costs $3.50 per gallon, how much will it cost to fill up the tank?
Solution:
def solution():
    miles_per_tank = 550
    price_per_gallon = 3.50
    gallons_per_mile = 1 / miles_per_tank
    cost_to_fill = price_per

print(solution())