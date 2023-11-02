def solution():
    # Calculate the amount of bronze needed for the three bells
    bronze_needed = 50 + (2*50) + (4*2*50)  # first bell is 50 pounds, second bell is twice the size of the first, third bell is four times the size of second
    result = bronze_needed
    return result

print(solution())