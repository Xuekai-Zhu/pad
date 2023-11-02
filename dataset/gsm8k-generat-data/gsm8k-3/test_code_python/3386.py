def solution():
    """A pair of dogs are barking back and forth at each other from across the street. The poodle barks twice for every one time the terrier barks. The terrier’s owner hushes it every second time it barks. She has to say “hush” six times before the dogs stopped barking. How many times did the poodle bark?"""
    # Define the ratio of barks between poodle and terrier
    POODLE_BARKS = 2
    TERRIER_BARKS = 1
    
    # Define the number of times the terrier was hushed
    hush_count = 6
    
    # Calculate the total number of barking rounds 
    total_rounds = hush_count * 2
    
    # Calculate the number of times the terrier barked
    terrier_barks = total_rounds // 3
    
    # Calculate the number of times the poodle barked
    poodle_barks = POODLE_BARKS * terrier_barks
    
    # Display the number of times the poodle barked
    result = poodle_barks
    return result

print(solution())