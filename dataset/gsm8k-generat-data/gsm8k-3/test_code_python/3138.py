def solution():
    """Milo's parents tell him that he can win cash rewards for good grades. He will get $5 times the average grade he gets. He gets three 2s, four 3s, a 4, and a 5. How much cash does he get?"""
    # Define the grades
    grades = [2, 2, 2, 3, 3, 3, 3, 4, 5]

    # Calculate the average grade
    avg_grade = sum(grades) / len(grades)

    # Calculate the cash reward
    cash_reward = avg_grade * 5

    # Display the cash reward
    result = cash_reward
    return result

print(solution())