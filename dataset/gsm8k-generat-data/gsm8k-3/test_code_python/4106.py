def solution():
    """Solomon collected three times as many cans as Juwan. Levi collected half of what Juwan collected. Solomon collected 66 cans. How many cans did the boys collect in all?"""
    # Define the number of cans Solomon collected
    solomon_cans = 66

    # Calculate the number of cans Juwan collected
    juwan_cans = solomon_cans // 3

    # Calculate the number of cans Levi collected
    levi_cans = juwan_cans // 2

    # Calculate the total number of cans collected
    total_cans = solomon_cans + juwan_cans + levi_cans

    # Display the total number of cans collected
    result = total_cans
    return result

print(solution())