def solution():
    """John is working as an IT specialist. He repairs broken computers. One day he had to fix 20 computers. 20% of them were unfixable, and 40% of them needed to wait a few days for spare parts to come. The rest John was able to fix right away. How many computers John was able to fix right away?"""
    # Define the number of computers that John had to fix
    total_computers = 20

    # Calculate the number of unfixable computers
    unfixable_computers = total_computers * 0.2

    # Calculate the number of computers that need to wait for spare parts
    waiting_computers = total_computers * 0.4

    # Calculate the number of computers that John was able to fix right away
    fixed_computers = total_computers - unfixable_computers - waiting_computers

    # Display the number of computers that John was able to fix right away
    result = fixed_computers
    return result

print(solution())