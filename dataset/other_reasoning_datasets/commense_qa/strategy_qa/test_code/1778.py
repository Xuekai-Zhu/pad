def solution():
    rosemary_songs = ["Love Grows (Where My Rosemary Goes)", "Randy Newman's Rosemary"]
    rose_songs = ["Kiss From a Rose", "The Rose", "Desert Rose", "Beauty of the Rose", "I Never Promised You a Rose Garden"]
    if len(rose_songs) > len(rosemary_songs):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())