def solution():
    # Calculate the number of hatchlings produced by 6 turtles
    eggs = 6 * 20  # 6 turtles each lay a clutch of 20 eggs
    hatchlings = int(0.4 * eggs)  # 40% of the eggs successfully hatch
    result = hatchlings
    return result

print(solution())