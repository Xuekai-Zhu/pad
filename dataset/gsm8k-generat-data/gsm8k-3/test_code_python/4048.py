def solution():
    """Ivanka wrote a book that took her 3 more months than it took Woody to write a book. Woody spent 1.5 years writing his book. How many months in total did Ivanka and Woody need to write their books?"""
    # Define Woody's writing time in months
    woody_time = 1.5 * 12

    # Define Ivanka's writing time in months
    ivanka_time = woody_time + 3

    # Calculate the total writing time in months
    total_time = woody_time + ivanka_time

    # Display the total writing time in months
    result = total_time
    return result

print(solution())