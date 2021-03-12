#!/usr/bin/python3

import json


images_to_test = json.load(open("images-to-test.json", "r"))


def get_names_of_modified_images(candidates):
    """Given a list of candidates, returns a set of modified Docker images."""
    names_of_modified_images = set()

    for candidate in candidates:
        c = candidate.split("/")[0]
        if c in images_to_test["image-versions"].keys():
            names_of_modified_images.add(c)

    return names_of_modified_images


def get_image_versions(candidates, delimiter):
    """Given a list of candidates, returns a list of images with versions."""
    return ["{}{}{}".format(i, delimiter, images_to_test["image-versions"][i]) for i in candidates]


def get_test_files(candidates):
    """Given a list of candidates, returns a list of test files."""
    return [images_to_test["tests"][i] for i in candidates]


if __name__ == "__main__":
    import argparse
    import sys
    parser = argparse.ArgumentParser(
        description="Looks up information about StaPH-B's Docker images in images-to-test.json.")
    parser.add_argument("--raw", "-r", action="store_true",
                        help="Convert raw image filepaths.")
    parser.add_argument("--versions-colon",
                        action="store_true", help="Get versions of images and append with a colon to image name.")
    parser.add_argument("--versions-slash",
                        action="store_true", help="Get versions of images and append with a slash to image name.")
    parser.add_argument("--get-test-files",
                        action="store_true", help="Get a list of shell scripts with which to test.")
    parser.add_argument("candidates", type=str, nargs="+",
                        help="Names of potential images.")
    args = parser.parse_args()
    if args.raw:
        print(" ".join(get_names_of_modified_images(args.candidates)))
    elif args.versions_colon:
        print(" ".join(get_image_versions(args.candidates, ":")))
    elif args.versions_slash:
        print(" ".join(get_image_versions(args.candidates, "/")))
    elif args.get_test_files:
        print(" ".join(get_test_files(args.candidates)))
