import sys
import os
from PIL import Image
from typing import List, Dict, Tuple

ImageData = List[Tuple[int, int, int]]
def load_matches() -> List[Dict[ImageData, float]]:

    matches: List[Dict[ImageData, float]] = []

    return matches

def main() -> None:
    
    if len(sys.argv) < 2:

        print("Expected at least input directory as parameter and got nothing!")
        exit(-1)

    #absolute path just in case
    path: str = os.path.abspath(sys.argv[1])

    if not os.path.isdir(path):

        print(f"Specified directory does not exist! ({path})")
        exit(-1)

    #check for tile matches
    #for now empty because I'm lazy but I'll make it work

    matches = load_matches()

    for img_path in os.listdir(path):
        
        parse_image(img_path, matches)

def parse_image(path_to_img: str, matches: List[Dict[ImageData, float]]) -> None:

    print(f"Path to image: {path_to_img}")

if __name__ == '__main__':
    main()
