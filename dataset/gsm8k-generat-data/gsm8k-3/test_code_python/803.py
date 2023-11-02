def solution():
    """ An elementary school teacher is making Halloween goodie bags for her class.  She wants the bags to be personalized, so she surveys her students asking whether they'd like a vampire-themed bag or a pumpkin-themed bag.  Of her 25 students, 11 indicate they want the vampire-themed bag and 14 indicate they want the pumpkin-themed bag.  The store the teacher shops at sells packs of 5 of each theme at a price of $3 per package, as well as individual bags of each theme at a price of $1 each.  What is the least amount of money the teacher can spend on the bags if she buys every student the theme they requested?"""

    # Define the number of students who want each theme
    vampire_students = 11
    pumpkin_students = 14

    # Calculate the number of packs of 5 needed for each theme
    vampire_packs = vampire_students // 5
    pumpkin_packs = pumpkin_students // 5

    # Calculate the number of individual bags needed for each theme
    vampire_remainder = vampire_students % 5
    pumpkin_remainder = pumpkin_students % 5

    # Calculate the total cost of each type of bag
    vampire_cost = (vampire_packs * 3) + (vampire_remainder * 1)
    pumpkin_cost = (pumpkin_packs * 3) + (pumpkin_remainder * 1)

    # Calculate the total cost for all the bags
    total_cost = vampire_cost + pumpkin_cost

    # Display the least amount of money the teacher can spend on the bags
    result = total_cost
    return result

print(solution())