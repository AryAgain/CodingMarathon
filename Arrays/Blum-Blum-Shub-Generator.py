"""
file: Blum-Blum-Shub-Generator.py
description: This program prints the first 63 bits of the generated output using Blum-Blum-Shub Generator
language: python3
author: AryAgain
"""


def main():
    seed = 40
    n = 307 * 491

    x_i_minus_one = seed

    first_63_bits = ''
    for i in range(1,64):
        xi = (x_i_minus_one**2) % n
        if xi % 2 == 0:
            first_63_bits += '0'
        else:
            first_63_bits += '1'
        x_i_minus_one = xi
    print('The first 63 bits of the generated output : ', first_63_bits)


if __name__ == '__main__':
    main()