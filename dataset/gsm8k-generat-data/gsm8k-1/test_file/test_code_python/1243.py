def solution():
    """Brendan has a bag of marbles with 10 inside. He tripped over a pebble while carrying it and dropped half of them.
    He scrambled to search for them but only came up with 3. When he went back home, he inspected the marbles further.
    One of them he picked up wasn't a marble, but actually a bead so he got rid of it. 
    How many marbles did Brendan end up with?"""
    
    initial_marbles = 10
    dropped_marbles = initial_marbles / 2
    found_marbles = 3
    non_marble = 1
    remaining_marbles = initial_marbles - dropped_marbles + found_marbles - non_marble
    result = remaining_marbles
    return result

print(solution())