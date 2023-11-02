def solution():
    """Mrs. Gable’s third grade class is on a field trip to the beach. For lunch, Mrs. Gable brought 20 lunches for the 20 students in her class. She included a pack of animal crackers in each lunch bag for dessert. Each pack of animal crackers contained 10 animal crackers. If 2 students did not eat their animal crackers, how many animal crackers were eaten in total among Mrs. Gable’s students?"""
    lunch_bags = 20
    animal_crackers_per_bag = 10
    total_animal_crackers = lunch_bags * animal_crackers_per_bag
    animal_crackers_not_eaten = 2 * animal_crackers_per_bag
    animal_crackers_eaten = total_animal_crackers - animal_crackers_not_eaten
    result = animal_crackers_eaten
    return result

print(solution())