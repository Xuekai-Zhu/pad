def solution():
    """Janet has 1/3 of a bottle of rose shampoo and 1/4 of a bottle of jasmine shampoo. If she uses 1/12 of a bottle of shampoo per day, how many days will her shampoo last?"""
    # Define the amount of shampoo Janet has
    rose_shampoo = 1/3
    jasmine_shampoo = 1/4

    # Calculate the total amount of shampoo Janet has
    total_shampoo = rose_shampoo + jasmine_shampoo

    # Calculate the number of days Janet's shampoo will last
    days = total_shampoo / (1/12)

    # Display the number of days
    result = days
    return result

print(solution())