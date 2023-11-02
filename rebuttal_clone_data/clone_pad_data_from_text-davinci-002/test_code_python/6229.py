def solution():
     drip_coffee = 2.25
     espresso = 3.50
     latte = 4.00
     vanilla_syrup = 0.50
     cold_brew = 2.50
     cappuccino = 3.50
     coffee_total = (drip_coffee * 2) + espresso + (latte * 2) + vanilla_syrup + (cold_brew * 2) + cappuccino
     result = coffee_total
     return result

print(solution())