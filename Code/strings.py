#!python
from utils import time_it

@time_it
def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text.
    time complexity: O(n*k)"""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement contains here (iteratively and/or recursively)
    # if text[:len(pattern)].lower() == pattern.lower():
    #     return True
    # else:
    #     if len(text) < len(pattern):
    #         return False
    #     return contains(text[1:], pattern)
    # return False
    if pattern == '':
        return True
    if len(text) < len(pattern):
        return False
    for i in range(len(text)):
        if (len(text)-i) < len(pattern):
            return False
        if text[i].lower() == pattern[0].lower():
            for j in range(len(pattern)):
                if text[i+j].lower() != pattern[j].lower():
                    break
                elif j == len(pattern)-1:
                    return True
    return False

@time_it
def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found.
    time complexity: O(n*k)"""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)
    # for i in range(len(text)):
    #     if text[i:i+len(pattern)] == pattern:
    #         return i
    # return None
    if pattern == '':
        return 0
    if len(text) < len(pattern):
        return None
    for i in range(len(text)):
        if (len(text)-i) < len(pattern):
            return None
        if text[i].lower() == pattern[0].lower():
            for j in range(len(pattern)):
                if text[i+j].lower() != pattern[j].lower():
                    break
                elif j == len(pattern)-1:
                    return i
    return None

@time_it
def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found.
    time complexity: O(n*k)"""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)
    indexes = list()
    # for i in range(len(text)):
    #     if text[i:i+len(pattern)] == pattern:
    #         indexes.append(i)
    # if indexes is not []:
    #     return indexes
    # return None
    if pattern == '':
        for i in range(len(text)):
            indexes.append(i)
        return indexes
    if len(text) < len(pattern):
        return indexes
    for i in range(len(text)):
        if (len(text)-i) < len(pattern):
            return indexes
        if text[i].lower() == pattern[0].lower():
            for j in range(len(pattern)):
                if text[i+j].lower() != pattern[j].lower():
                    break
                elif j == len(pattern)-1:
                    indexes.append(i)
    if indexes != []:
        return indexes
    return indexes

def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    print(find_all_indexes('zzz', ''))
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
