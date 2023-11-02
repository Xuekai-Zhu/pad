def solution():
    """Three times as many children as adults attend a concert on Saturday. An adult ticket costs $7 and a child's ticket costs $3. The theater collected a total of $6,000. How many people bought tickets?"""
    # Let's assume the number of adults be A, and the number of children be C
    # Finding equations
    # C = 3A,                       (1) because the number of children is three times the number of adults.
    # 7A + 3C = 6000,                  (2) because the total amount collected from Adults and Children is $6000

    # Substituting eq (1) in eq (2)
    # 7A + 3(3A) = 6000
    # 16A = 6000
    # A = 375

    # The number of children
    C = 3 * 375

    # The total number of people
    total_people = A + C

    # Return the result
    result = total_people
    return result

print(solution())