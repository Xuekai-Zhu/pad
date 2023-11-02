def solution():
    total_candy = 418
    taquon_candy = 171
    mack_candy = 171

    # Calculate the total candy that Taquon and Mack had together
    taquon_mack_candy = taquon_candy + mack_candy

    # Calculate the candy that Jafari had
    jafari_candy = total_candy - taquon_mack_candy
    result = jafari_candy
    return result

print(solution())