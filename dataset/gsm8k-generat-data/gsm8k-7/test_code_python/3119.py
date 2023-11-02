def solution():
    num_cans = 60
    can_size_before_compaction = 30
    compaction_ratio = 0.2

    # Calculate the total size of all cans before compaction
    total_size_before_compaction = num_cans * can_size_before_compaction

    # Calculate the size of all cans after compaction
    size_after_compaction = total_size_before_compaction * compaction_ratio

    result = size_after_compaction
    return result

print(solution())