def solution():
    """There is a playground that is surrounded by a square fence that has a side length of 27 yards. There is a 12 yard by 9 yard garden that has fencing around it. How many yards of fencing do the playground and garden have together?"""
    # Calculate the perimeter of the playground fence
    playground_perimeter = 4 * 27

    # Calculate the perimeter of the garden fence
    garden_perimeter = 2*(12 + 9)

    # Calculate the total fencing required
    total_fencing = playground_perimeter + garden_perimeter

    # Display the total fencing required
    result = total_fencing
    return result

print(solution())