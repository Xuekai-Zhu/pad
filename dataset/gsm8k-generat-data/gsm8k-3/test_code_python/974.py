def solution():
    """Jessie invited 4 friends over to play. They made muffins for a snack and Jesse wants to divide them equally between herself and her friends. If they made 20 muffins in total, how many will each person have? """
    # Define the total number of muffins made
    total_muffins = 20

    # Define the number of people who will share the muffins
    num_people = 5 # Jessie and her 4 friends

    # Calculate the number of muffins each person will have
    muffins_per_person = total_muffins // num_people

    # Display the number of muffins each person will have
    result = muffins_per_person
    return result

print(solution())