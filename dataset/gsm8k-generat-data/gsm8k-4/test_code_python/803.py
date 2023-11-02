def solution():
    """An elementary school teacher is making Halloween goodie bags for her class. She wants the bags to be personalized, so she surveys her students asking whether they'd like a vampire-themed bag or a pumpkin-themed bag. Of her 25 students, 11 indicate they want the vampire-themed bag and 14 indicate they want the pumpkin-themed bag. The store the teacher shops at sells packs of 5 of each theme at a price of $3 per package, as well as individual bags of each theme at a price of $1 each. What is the least amount of money the teacher can spend on the bags if she buys every student the theme they requested?"""
    # Define the number of students who want a vampire-themed bag and a pumpkin-themed bag
    vampire_students = 11
    pumpkin_students = 14

    # Calculate the number of packages needed for each theme
    vampire_packages = (vampire_students // 5) + (1 if vampire_students % 5 != 0 else 0)
    pumpkin_packages = (pumpkin_students // 5) + (1 if pumpkin_students % 5 != 0 else 0)

    # Calculate the total cost of purchasing packages of bags
    package_cost = (vampire_packages + pumpkin_packages) * 3

    # Calculate the number of individual bags needed for each theme
    vampire_individual = vampire_students % 5
    pumpkin_individual = pumpkin_students % 5

    # Calculate the total cost of purchasing individual bags
    individual_cost = (vampire_individual + pumpkin_individual) * 1

    # Calculate the total cost of all bags
    total_cost = package_cost + individual_cost

    # Return the least amount spent on the bags
    result = total_cost
    return result

print(solution())