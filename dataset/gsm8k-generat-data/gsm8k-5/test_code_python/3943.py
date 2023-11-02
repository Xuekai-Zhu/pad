def solution(): 
    # Original number of necklaces and earrings
    original_necklaces = 10
    original_earrings = 15

    # Jessy buys more necklaces and earrings
    additional_necklaces = 10
    additional_earrings = (2/3) * original_earrings
    
    # Total number after Jessy's purchase
    total_necklaces = original_necklaces + additional_necklaces
    total_earrings = original_earrings + additional_earrings

    # Jessy's mother gives her even more earrings
    additional_earrings2 = (1/5) * total_earrings
    total_earrings += additional_earrings2

    # Calculate the total number of jewelry pieces Jessy has
    total_jewelry = total_necklaces + total_earrings
    result = total_jewelry
    return result

print(solution())