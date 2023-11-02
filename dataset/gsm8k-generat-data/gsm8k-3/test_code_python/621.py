def solution():
    """There are 36 seagulls on the roof of the Taco Bell. Kids scare 1/4 of them away by throwing stones, and 1/3 of the remaining birds decide to fly to McDonald's parking lot. How many seagulls are left?"""
    # Define the starting number of seagulls
    starting_seagulls = 36

    # Calculate the number of seagulls scared away by kids
    scared_seagulls = starting_seagulls // 4

    # Calculate the number of remaining seagulls
    remaining_seagulls = starting_seagulls - scared_seagulls

    # Calculate the number of seagulls that flew to McDonald's parking lot
    flew_away_seagulls = remaining_seagulls // 3

    # Calculate the final number of seagulls
    final_seagulls = remaining_seagulls - flew_away_seagulls

    # Display the final number of seagulls
    result = final_seagulls
    return result

print(solution())