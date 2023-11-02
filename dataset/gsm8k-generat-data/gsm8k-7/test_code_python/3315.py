def solution():
    num_cars_planned = 200
    metal_shortage = 50
    pandemic_cut = 0.5

    # Calculate the number of cars produced after metal shortage
    num_cars_after_metal_shortage = num_cars_planned - metal_shortage

    # Calculate the number of cars produced after pandemic cut
    num_cars_after_pandemic_cut = num_cars_after_metal_shortage * (1 - pandemic_cut)

    # Calculate the total number of doors produced
    num_doors_produced = num_cars_after_pandemic_cut * 5
    result = num_doors_produced
    return result

print(solution())