def solution():
    
    elephant_count = 20
    hippo_count = 35
    new_hippo_count = (5/7) * hippo_count * 5
    new_elephant_count = new_hippo_count + 10
    total_animals = elephant_count + hippo_count + new_hippo_count + new_elephant_count
    result = total_animals
    return result

print(solution())