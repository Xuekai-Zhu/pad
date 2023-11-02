def solution():
    total_oranges = 180  # They sold a total of 180 oranges
    alices_oranges = 0  # Let's initialize Alice's oranges to 0 for now

    # Let's use a loop to try out different numbers of oranges that Emily could have sold
    for emilys_oranges in range(1, total_oranges):
        # If Alice sold twice as many oranges as Emily, we can calculate Alice's oranges
        if alices_oranges == 2 * emilys_oranges:
            break
        alices_oranges = total_oranges - emilys_oranges  # Update Alice's oranges
    result = alices_oranges
    return result

print(solution())