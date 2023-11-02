def solution():
    """There are 3 numbers that are consecutive integers. Together they have a sum of 18. What is the largest of the 3 numbers?"""
    # Define the sum and number of consecutive integers
    total_sum = 18
    num_integers = 3

    # Calculate the average value of the consecutive integers
    average = total_sum / num_integers

    # Calculate the largest of the 3 numbers
    largest = int(average + 1)

    # return the result
    result = largest
    return result

print(solution())