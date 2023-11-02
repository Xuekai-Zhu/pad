def solution():
    """Mason needs 30 ounces of sugar to make a batch of suckers and 70 ounces of sugar to make a batch of fudge. How much sugar does he need to make 8 batches of suckers and 1 batch of fudge?"""
    sugar_per_sucker_batch = 30
    sugar_per_fudge_batch = 70
    num_sucker_batches = 8
    num_fudge_batches = 1
    total_sugar = (sugar_per_sucker_batch * num_sucker_batches) + (sugar_per_fudge_batch * num_fudge_batches)
    result = total_sugar
    return result

print(solution())