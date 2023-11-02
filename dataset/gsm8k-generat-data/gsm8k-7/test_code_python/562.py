def solution():
    mom_dog_food = 1.5 * 3 # cups of food per day
    puppy_food = 0.5 * 2 * 5 # cups of food per day for all puppies
    total_food_needed = (mom_dog_food + puppy_food) * 6 # total food needed for 6 days
    result = total_food_needed
    return result

print(solution())