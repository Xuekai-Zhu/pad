def solution():
    """A pair of dogs are barking back and forth at each other from across the street. The poodle barks twice for every one time the terrier barks. The terrier’s owner hushes it every second time it barks. She has to say “hush” six times before the dogs stopped barking. How many times did the poodle bark?"""
    poodle_bark_per_terrier_bark = 2
    total_terrier_barks = 6
    terrier_barks_before_hush = 2
    poodle_barks = poodle_bark_per_terrier_bark * total_terrier_barks
    total_hushes = total_terrier_barks / terrier_barks_before_hush
    poodle_barks_stopped = total_terrier_barks + total_hushes
    result = poodle_barks_stopped
    
    return result

print(solution())