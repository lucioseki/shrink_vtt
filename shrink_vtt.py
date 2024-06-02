#!/usr/bin/env python3
"""
Tool to shrink a Zoom-generated VTT file by merging sequential captions from the same person.
"""

import argparse
import webvtt

def main(file_name: str):
    """
    Main function
    """
    vtt = webvtt.read(file_name)
    for caption in vtt.captions:
        person = caption.text.split(':', maxsplit=1)[0]
        caption.person = person.strip()

    shrinked_captions = []
    i = 0
    new_caption = vtt.captions[0]
    while i < len(vtt.captions)-1:
        next_caption = vtt.captions[i+1]
        while new_caption.person == next_caption.person:
            new_caption.text += next_caption.text.split(':', maxsplit=1)[1]
            new_caption.end = next_caption.end
            i += 1
            if i > len(vtt.captions):
                break
            next_caption = vtt.captions[i+1]

        new_caption.identifier = str(len(shrinked_captions) + 1)
        shrinked_captions.append(new_caption)

        i += 1
        new_caption = vtt.captions[i]

    vtt.captions = shrinked_captions

    with open(f'shrink.{file_name}', 'w', encoding='utf-8') as f:
        vtt.write(f)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='A tool to trim Zoom-generated WebVTT file')
    parser.add_argument(
        'filename',
        help='Name of the VTT file to be processed')
    args = parser.parse_args()
    main(args.filename)
