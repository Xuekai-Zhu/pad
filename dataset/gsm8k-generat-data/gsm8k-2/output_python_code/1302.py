def solution():
    """Terry spent 6$ for breakfast on Monday, twice as much on Tuesday, and on Wednesday Terry spent double what he did the previous two days combined. How much did Terry spend total?"""
    monday_spent = 6
    tuesday_spent = 2 * monday_spent
    wednesday_spent = 2 * (monday_spent + tuesday_spent)
    total_spent = monday_spent + tuesday_spent + wednesday_spent
    result = total_spent
    return result

print(solution())