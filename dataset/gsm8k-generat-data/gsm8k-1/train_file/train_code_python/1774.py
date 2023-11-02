def solution():
    """One student on a field trip counted 12 squirrels. Another counted a third more squirrels than the first student. How many squirrels did both students count combined?"""
    first_count = 12
    second_count = first_count + (first_count / 3)
    total_count = first_count + second_count
    result = total_count
    return result

print(solution())