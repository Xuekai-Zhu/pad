def solution():
     total_items = 22
     packets_of_drink_mix = 3 * tent_stakes
     bottles_of_water = 2 + tent_stakes
     total = packets_of_drink_mix + bottles_of_water + tent_stakes
     tent_stakes = (total - (packets_of_drink_mix + bottles_of_water)) / 2
     result = tent_stakes
     return result

print(solution())