def solution():
    """Paddy's Confidential has 600 cans of stew required to feed 40 people. How many cans would be needed to feed 30% fewer people?"""
    # Define the initial number of cans and people
    cans = 600
    people = 40

    # Calculate the number of cans per person
    cans_per_person = cans / people

    # Calculate the number of people with a 30% decrease
    new_people = int(people * 0.7)

    # Calculate the total number of cans needed for the new number of people
    new_cans = cans_per_person * new_people

    # Display the total number of cans needed
    result = new_cans
    return result

print(solution())