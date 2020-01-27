#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # TODO: Decode digits from binary (base 2)
    result = 0
    # digits = digits[::-1]
    # digits = digits.split(".")
    # if(len(digits) == 1):
    #     for i in range(len(digits)):
    #         result += (int(digits[i], base)*(base**i))
    #     return result
    # if(len(digits) == 2):
    #     for i in range(len(digits[1])):
    #         result += (int(digits[1][i], base)*(base**i))
    #     for j in range(len(digits[0])):
    #         result += (int(digits[0][j], base)*(base**(-(j+1))))
    # return result
    highest_power = len(digits.split(".")[0])-1
    digits = digits.replace(".", "")
    for i in range(len(digits)):
        result += (int(digits[i], base)*(base**highest_power))
        highest_power -= 1
    return result


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    # TODO: Encode number in binary (base 2)
    # TODO: Encode number in hexadecimal (base 16)
    # TODO: Encode number in any base (2 up to 36)
    useable_digits = string.digits + string.ascii_lowercase
    result = ""
    if base <= 1:
        return number
    remainder = number % base
    quotient = number / base
    while quotient > 0:
        result = useable_digits[remainder] + result
        remainder = int(quotient) % base
        quotient = int(quotient) / base
    return result

def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # TODO: Convert digits from base 2 to base 16 (and vice versa)
    deci = decode(digits, base1)
    return encode(deci, base2)


def main():
    """Read command-line arguments and convert given digits between bases."""
    print(decode("1101.101", 2))
    print(encode(13.625, 2))
    print(encode(4.47, 2))
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
