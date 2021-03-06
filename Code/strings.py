#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement contains here (iteratively and/or recursively)

    # O(m * n)

    index = find_index(text, pattern)

    return index is not None



def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)

    # O(m * n)


    starting_index = 0

    i = 0
    j = 0

    # B A N A N A S
    # N A S

    if len(text) == 0 or len(pattern) == 0:
    	return 0

    while i < len(text):
    	print(starting_index)
    	if text[i] == pattern[j]:
    		j += 1
    		i += 1
    		if j == len(pattern):
    			return starting_index
    	else:
    		starting_index += 1
    		i = starting_index
    		j = 0

    return None

def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)

    # O(m * n)

    indicies = []

    starting_index = 0

    i = 0
    j = 0

    # A A A
    # A A 

    if len(text) == 0 or len(pattern) == 0:
    	return [i for i in range(len(text))]

    while i < len(text):
        if text[i] == pattern[j]:
            j += 1
            i += 1
            if j == len(pattern):
                j = 0
                indicies.append(starting_index)
                i = starting_index + 1
                starting_index = i
        else:
            starting_index += 1
            i = starting_index
            j = 0

    return indicies


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
