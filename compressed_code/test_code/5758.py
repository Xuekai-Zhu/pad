def solution():
    
    batch_size = 65
    num_batches = 45
    removed_cupcakes = 5 * num_batches
    total_cupcakes = batch_size * num_batches
    remaining_cupcakes = total_cupcakes - removed_cupcakes
    num_people = 19 + 1  
    cupcakes_per_person = remaining_cupcakes // num_people
    result = cupcakes_per_person
    return result

print(solution())