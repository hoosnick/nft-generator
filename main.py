import os
import itertools
import uuid
from PIL import Image


class NFT_Generator:
    def __init__(self, folder_name: str) -> None:
        self.folder_name = folder_name

    def includes(self):
        self.bg = self.change_dir('bg')
        self.eyes = self.change_dir('eyes')
        self.mouth = self.change_dir('mouth')
        self.head = self.change_dir('head')

        collection = list(
            itertools.product(
                self.bg,
                self.eyes,
                self.mouth,
                self.head
            )
        )
        print(f'Count: {len(collection)}')

        return collection

    @staticmethod
    def change_dir(name: str):
        path = [f"includes/{name}/{f}" for f in os.listdir(f'includes/{name}')]
        return path

    def generate(self):
        collections = self.includes()

        if not os.path.isdir(self.folder_name):
            os.makedirs(self.folder_name)

        n, m = 1, len(collections)
        for c in collections:
            source = list(c)
            name = str(uuid.uuid4())
            bg, eye, mouth, head = source

            img = Image.open(bg)
            head = Image.open(head)
            eye = Image.open(eye)
            mouth = Image.open(mouth)
            img = img.convert("RGBA")
            head = head.convert("RGBA")
            eye = eye.convert("RGBA")
            mouth = mouth.convert("RGBA")

            img.paste(head, (0, 0), head)
            img.paste(eye, (0, 0), eye)
            img.paste(mouth, (0, 0), mouth)

            img.save(self.folder_name + '/' + name + '.png', format='png')
            print(f'[{n}/{m}] New {name}.png created!')
            n += 1
        else:
            print('The end!')


if __name__ == '__main__':
    nft_mkr = NFT_Generator('new_folder_name')
    nft_mkr.generate()
