def solution():
     novels = 145
     comics = 271
     documentaries = 419
     albums = 209
     items_per_crate = 9
     total_items = novels + comics + documentaries + albums
     total_crates = total_items / items_per_crate
     result = total_crates
     return result

print(solution())