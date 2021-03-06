#!/usr/bin/env python3

# Created by: Paterry Baptichon
# Created on: 2022-05-01
# This program can show the user the rgb values
def main():
    r = 0
    b = 0
    g = 0
    # loop adds 1 to r and goes until it hits 255
    while r <= 255:
        # loop adds 1 to g until it hits 255
        while g <= 255:
            # loop adds 1 to b until it hits 255
            while b <= 255:
                print("\033[1;38;2;{0};{1};{2}mRGB({0}, {1}, {2})".format(r, g, b))
                b += 1
            g += 1
            # resets b
            b = 0
        r += 1
        # resets b and g
        b = 0
        g = 0

if __name__ == "__main__":
    main()
