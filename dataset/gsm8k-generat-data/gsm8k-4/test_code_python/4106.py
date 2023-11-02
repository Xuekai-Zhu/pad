def solution():
    """Solomon collected three times as many cans as Juwan. Levi collected half of what Juwan collected. Solomon collected 66 cans. How many cans did the boys collect in all?"""
    # Define the number of cans collected by Solomon
    solomon_cans = 66

    # Calculate the number of cans collected by Juwan
    juwan_cans = solomon_cans / 3

    # Calculate the number of cans collected by Levi
    levi_cans = juwan_cans / 2

    # Calculate the total number of cans collected by the boys
    total_cans = solomon_cans + juwan_cans + levi_cans

    result = total_cans
    return result

print(solution())