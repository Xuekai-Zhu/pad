def solution():
    s_mores_per_person = 3  # Each person will eat 3 S'mores
    total_people = 8  # There are 8 people in total
    s_mores_needed = s_mores_per_person * total_people  # Calculate the total number of S'mores needed
    s_mores_per_pack = 4  # Each pack can make 4 S'mores
    packs_needed = s_mores_needed // s_mores_per_pack + (1 if s_mores_needed % s_mores_per_pack != 0 else 0)  # Round up to the nearest pack
    cost_per_pack = 3  # It costs $3 to make 4 S'mores
    total_cost = packs_needed * cost_per_pack  # Calculate the total cost of supplies

    result = total_cost
    return result

print(solution())