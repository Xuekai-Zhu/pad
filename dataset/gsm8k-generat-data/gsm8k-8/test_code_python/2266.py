def solution():
    # Define Haley's number of necklaces
    haley_necklaces = 25

    # Calculate Jason's number of necklaces
    jason_necklaces = haley_necklaces - 5

    # Calculate Josh's number of necklaces
    josh_necklaces = jason_necklaces / 2

    # Calculate the difference between Haley's and Josh's number of necklaces
    difference = haley_necklaces - josh_necklaces
    result = difference
    return result

print(solution())