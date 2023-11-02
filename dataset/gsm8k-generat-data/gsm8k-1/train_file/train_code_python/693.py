def solution():
    """If one fourth of the engines are defective, and there are 5 batches of 80 engines each. How many engines are not defective?"""
    num_batches = 5
    num_engines_per_batch = 80
    num_defective_engines = (1/4) * num_engines_per_batch
    num_total_defective_engines = num_defective_engines * num_engines_per_batch * num_batches
    num_non_defective_engines = (num_engines_per_batch - num_defective_engines) * num_engines_per_batch * num_batches
    result = num_non_defective_engines
    return result

print(solution())