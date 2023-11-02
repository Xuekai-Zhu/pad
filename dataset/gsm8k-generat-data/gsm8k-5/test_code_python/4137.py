def solution():
    diego_cakes = 12  # Diego baked 12 cakes
    donald_cakes = 4  # Donald baked 4 cakes
    donald_cakes -= 1  # Donald ate 1 cake while waiting for the party
    total_cakes = diego_cakes + donald_cakes  # Calculate the total number of cakes left
    result = total_cakes
    return result

print(solution())