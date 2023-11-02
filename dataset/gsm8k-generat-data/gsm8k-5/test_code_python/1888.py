def solution():
    total_streetlights = 200  # The city council bought 200 streetlights
    total_squares = 15  # There are 15 squares in New York
    streetlights_per_square = 12  # Each square will have 12 new streetlights

    # Calculate the total number of streetlights that will be used in all the squares
    streetlights_used = total_squares * streetlights_per_square

    # Calculate the number of unused streetlights
    unused_streetlights = total_streetlights - streetlights_used
    result = unused_streetlights
    return result

print(solution())