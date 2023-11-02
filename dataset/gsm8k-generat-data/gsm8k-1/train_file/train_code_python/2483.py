def solution():
    """There are 3 rows of people relaxing at the beach. The first row is made up of 24 people until 3 people get up to wade in the water. 5 people from the second row, which originally held 20 people, go to join them. The third row is made up of 18 people. How many people are left relaxing on the beach?"""
    row1_initial = 24
    row1_missing = 3
    row2_initial = 20
    row2_missing = 5
    row3_initial = 18
    total_relaxing = row1_initial + row2_initial + row3_initial
    total_missing = row1_missing + row2_missing
    remaining_relaxing = total_relaxing - total_missing
    result = remaining_relaxing
    return result

print(solution())