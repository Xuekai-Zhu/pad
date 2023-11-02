def solution():
    """Three different 6th grade classes are combining for a square dancing unit.
    If possible, the teachers would like each male student to partner with a female student for the unit.
    The first class has 17 males and 13 females, while the second class has 14 males and 18 females,
    and the third class has 15 males and 17 females. When the classes are combined,
    how many students will be unable to partner with a student of the opposite gender?"""
    # Define the number of males and females in each class
    class1 = {"males": 17, "females": 13}
    class2 = {"males": 14, "females": 18}
    class3 = {"males": 15, "females": 17}

    # Calculate the total number of males and females
    total_males = class1["males"] + class2["males"] + class3["males"]
    total_females = class1["females"] + class2["females"] + class3["females"]

    # Determine the minimum number of pairs that can be formed
    min_pairs = min(total_males, total_females)

    # Calculate the number of students that will be unable to partner with a student of the opposite gender
    remaining_males = total_males - min_pairs
    remaining_females = total_females - min_pairs
    unable_to_partner = abs(remaining_males - remaining_females)

    # Display the number of students unable to partner
    result = unable_to_partner
    return result

print(solution())