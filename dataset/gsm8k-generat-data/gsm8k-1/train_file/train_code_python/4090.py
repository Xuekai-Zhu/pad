def solution():
    """Ryan works in an office that has an even number of men and women working there. Ryan participates in a meeting composed of 4 men and 6 women who are pulled from the office floor. This reduces the number of women working on the office floor by 20%. How many people work at Ryan's office?"""
    men_at_office = women_at_office = number_of_people = 0
    
    # Since the office has even number of men and women, their count will be equal
    while men_at_office == 0 or men_at_office % 2 != 0:
        # Asking the user for the number of people in the office until an even number is given
        number_of_people = int(input("Enter the number of people in Ryan's office (even number): "))
        men_at_office = women_at_office = number_of_people / 2
    
    # Calculating the number of women remaining on the office floor after the meeting
    women_at_office = women_at_office - (6 * 0.2)
    
    return int(number_of_people)

print(solution())