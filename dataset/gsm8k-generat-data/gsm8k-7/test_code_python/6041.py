def solution():
    num_novels = 145
    num_comics = 271
    num_documentaries = 419
    num_albums = 209
    crate_size = 9

    # Calculate the total number of items that Natalia wants to store
    total_items = num_novels + num_comics + num_documentaries + num_albums

    # Calculate the number of crates needed to store all the items
    num_crates = total_items // crate_size

    # Add an extra crate if there are any items left over
    if total_items % crate_size != 0:
        num_crates += 1

    result = num_crates
    return result

print(solution())