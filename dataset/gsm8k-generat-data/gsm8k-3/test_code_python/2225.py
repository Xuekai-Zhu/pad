def solution():
    """Mario's salary increased by 40% to $4000 this year. Bob's salary from last year was equal to three times Mario's salary this year. If Bob's current salary is 20% more than his salary last year, what is his current salary?"""
    # Define Mario's salary and his salary increase
    mario_salary = 4000
    mario_increase = 0.4

    # Calculate Mario's salary last year
    mario_last_year = mario_salary / (1 + mario_increase)

    # Calculate Bob's salary last year
    bob_last_year = 3 * mario_last_year

    # Calculate Bob's current salary
    bob_current = bob_last_year * 1.2

    # Display Bob's current salary
    result = bob_current
    return result

print(solution())