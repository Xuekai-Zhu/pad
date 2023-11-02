def solution():
    """Aston has accidentally torn apart his comics and needs to put all the pages back together. Each comic has 25 pages and Aston has found 150 pages on the floor. He puts his comics back together and adds them back into his box of comics. If there were already 5 untorn comics in the box, how many comics are now in the box of comics?"""
    pages_per_comic = 25
    total_pages = 150
    comics_from_pages = total_pages // pages_per_comic
    total_comics = comics_from_pages + 5
    result = total_comics
    return result

print(solution())