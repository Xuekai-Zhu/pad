def solution():
    """Mrs. Gable’s third grade class is on a field trip to the beach. For lunch, Mrs. Gable brought 20 lunches for the 20 students in her class. She included a pack of animal crackers in each lunch bag for dessert. Each pack of animal crackers contained 10 animal crackers. If 2 students did not eat their animal crackers, how many animal crackers were eaten in total among Mrs. Gable’s students?"""
    num_students = 20
    num_packs = num_students
    crackers_per_pack = 10
    num_unopened_packs = 2
    num_opened_packs = num_packs - num_unopened_packs
    total_crackers = num_opened_packs * crackers_per_pack
    result = total_crackers
    return result

print(solution())