"""
@author Haotian Weng
@email haotian.weng@anu.edu.au
@create date 2021-06-19
@modify date 2021-06-19
@desc Sequentially generate unique Onion URLs
"""

import itertools

# Onion URLs consist of [2-7] and [a-z]
CHARS = "234567abcdefghijklmnopqrstuvwxyz"


def generate_urls(version=2, file_path="../data/onion_urls.txt"):
    """Sequentially generate unique Onion URLs and output them to a file.
        v2 Onion URLs are 16-character alpha-semi-numeric hashes.
        v3 Onion URLs are 56-character alpha-semi-numeric hashes.
        https://tb-manual.torproject.org/onion-services/

    Args:
        version (int, optional): [The version of Onion URLs]. Defaults to 2. Can be either 2 or 3.
        file_path (str, optional): [The output file path]. Defaults to "../data/onion_urls.txt".

    Raises:
        ValueError: [Wrong version number]
    """
    # Set URL length
    if version == 2:
        url_len = 16
    elif version == 3:
        url_len = 56
    else:
        raise ValueError("The version of Onion URLs must be either 2 or 3!")

    with open(file_path, "wt+") as f:
        # Sequentially generate unique Onion URLs
        for c in itertools.product(CHARS, repeat=url_len):
            f.write("".join(c) + ".onion" + "\n")


if __name__ == "__main__":
    # Test run
    generate_urls()
