def solution():
    initial_jellybeans = 37  # There were 37 jellybeans in the jar
    removed_jellybeans = 15  # Pat removed 15 jellybeans
    added_jellybeans = 5  # Pat added 5 of the removed jellybeans back in
    final_removed_jellybeans = 4  # Pat removed 4 more jellybeans

    # Calculate the number of jellybeans in the jar after each step
    jellybeans_after_removal = initial_jellybeans - removed_jellybeans
    jellybeans_after_addition = jellybeans_after_removal + added_jellybeans
    jellybeans_after_final_removal = jellybeans_after_addition - final_removed_jellybeans
    result = jellybeans_after_final_removal
    return result

print(solution())