def solution():
    """Jared likes to draw monsters. He drew a monster family portrait. The mom had 1 eye and the dad had 3. They had 3 kids, each with 4 eyes. How many eyes did the whole family have?"""
    # Define the number of eyes for each family member
    mom_eyes = 1
    dad_eyes = 3
    kid_eyes = 4

    # Calculate the total number of eyes in the family
    total_eyes = mom_eyes + dad_eyes + (3 * kid_eyes)

    # Display the total number of eyes
    result = total_eyes
    return result

print(solution())