def solution():
    first_scroll_age = 4080  # The first scroll is 4080 years old
    previous_scroll_age = first_scroll_age  # Set the age of the previous scroll to be the age of the first scroll

    # Loop through the remaining scrolls to calculate their ages based on the age of the previous scroll
    for i in range(2, 6):
        current_scroll_age = previous_scroll_age * 1.5  # Each scroll is older than the previous scroll by half as many years as the previous scroll's age
        previous_scroll_age = current_scroll_age  # Set the age of the current scroll to be the age of the previous scroll for the next iteration

    fifth_scroll_age = current_scroll_age  # The age of the fifth scroll is the age of the current scroll after the loop has finished
    result = fifth_scroll_age
    return result

print(solution())