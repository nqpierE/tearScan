import sys
from tear import Tear


def main():
    new_tear: Tear = Tear()
    new_tear.root_url = "https://qiita.com/Terao-Takumi/items/ff3974c6c5baf723797f"
    new_tear.word = "qiita"
    response = new_tear.startTear()
    for i in response:
        print(i)


if __name__ == "__main__":
    main()
