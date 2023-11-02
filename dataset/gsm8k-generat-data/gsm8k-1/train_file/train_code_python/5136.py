def solution():
    """Stoney Hollow Middle School is taking a field trip to the zoo. There are 109 fifth graders, 115 sixth graders, and 118 seventh graders. There are 4 teachers and 2 parents from each grade coming along to chaperone on the trip. There are 72 seats on each school bus. How many buses are needed for the field trip?"""
    fifth_graders = 109
    sixth_graders = 115
    seventh_graders = 118
    teachers_per_grade = 4
    parents_per_grade = 2
    total_passengers = (fifth_graders + sixth_graders + seventh_graders + 
                        teachers_per_grade * 3 + parents_per_grade * 3)
    buses_needed = (total_passengers // 72) + 1  # round up to nearest whole number
    result = buses_needed
    return result

print(solution())