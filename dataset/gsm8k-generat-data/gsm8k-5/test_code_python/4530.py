def solution():
    total_items = 40
    ella_incorrect = 4  # Ella got 4 incorrect answers
    ella_correct = total_items - ella_incorrect
    marion_correct = ella_correct - 6  # Marion got 6 less than Ella's correct answers
    marion_score = marion_correct / total_items * 100  # Convert to percentage
    result = marion_score
    return result

print(solution())