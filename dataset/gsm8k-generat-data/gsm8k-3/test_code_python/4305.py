def solution():
    """Gabrielle sells eggs. On Monday she sells 5 crates of eggs. On Tuesday she sells 2 times as many crates of eggs as Monday. On Wednesday she sells 2 fewer crates than Tuesday. On Thursday she sells half as many crates of eggs as she sells on Tuesday. How many total crates of eggs does she sell for the 4 days?"""
    # Define the number of crates sold on each day
    monday = 5
    tuesday = 2 * monday
    wednesday = tuesday - 2
    thursday = tuesday / 2

    # Calculate the total number of crates sold over the four days
    total_crates = monday + tuesday + wednesday + thursday

    # Display the total number of crates sold
    result = total_crates
    return result

print(solution())