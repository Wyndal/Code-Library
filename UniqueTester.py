

def is_unique(string):
    hash_table = [None] * len(string)

    for char in string:

        # Getting index that character hashes to
        hash_index = __recursive_hash(char, len(string), hash_table)

        # if the hash is
        if hash_index == -1:
            return False

        # storing the character into the hash table
        hash_table[hash_index] = char

    return True



def __recursive_hash(char, string_length, hash_table, seed=0):
    result_index = (ord(char) + seed) % string_length

    # checking to see if the index is taken
    if hash_table[result_index] is not None:

        # turns out it is taken, now we check to see if it is not taken by an equal character
        if hash_table[result_index] is char:

            # it is taken by an equal character, therefore the string is not unique
            return -1
        else:

            # we have to rehash and try for a new index
            __recursive_hash(char, string_length, hash_table, seed+1)


    # the index is not taken, so give it to this character
    return result_index

