"""
Functions to manipulate the Linux words file. 
"""
import urllib.request



# Treat this function as a black box. It does not need to be modified. 
def get_word_list(path=None):
    """
    Download word_list.txt from GitHub. 

    Parameters
    ----------
    path: str
        If data cannot be downloaded from GitHub, load locally from file.

    Returns
    -------
    list
        List of words that comprise the Linux dictionary file. 
    """
    if path is None:
        words = []
        url = "https://gist.githubusercontent.com/jtrive84/b8eaedc6ae52ed0fb2551094bd772bc6/raw/c2ced4a03f7bc8dc512222df77c291ad480b9d25/word_list.txt"
        for line in urllib.request.urlopen(url):
            words.append(line.strip().decode('utf-8'))
    else:
        # Load words file from disk.
        with open(path, "r") as ff:
            words = [line.rstrip() for line in ff]
    return words




# ------------------------------------------------------------------------------
# Part 1: Complete preprocess function. When finished, test your function
# by uncommenting and running `test_preprocess`.
# -----------------------------------------------------------------------------

def preprocess():
    """
    Pre-process word list, returning a filtered list of pre-processed words.
        1. Remove whitespace from all words in list.
        2. Convert all words to lower case.
        3. Remove any words with single quote (').

    Returns
    -------
    list
        List of words in lowercase with apostrophes removed. 
    """
    # Load initial words list by calling get_word_list. 
    word_list = get_word_list()

    ### TODO ###################################################################
    # - Create a new empty list named word_list2. 
    #
    # - Iterate (loop over) each word in word_list, removing whitespace 
    #   (`.strip()`) and converting each to lowercase. (`.lower()`). 
    #
    # - If word contains an apostrophe ('), do not append it to word_list2. 
    #
    # - All remaining words should be appended to word_list2. 
    #
    # - Replace the empty returned list with your newly created list.
    #
    # - Requires 5-8 LOCs (excluding comments). 
    #
    ####################### YOUR CODE HERE #####################################
    word_list2 = []

    for word in word_list:

        # Strip whitespace and convert to lowercase. 
        word = word.strip().lower()

        # Check if word contains an apostrophe. If it does, do not 
        # append to word_list2. 
        if "'" not in word:
            word_list2.append(word)

    return word_list2
    





# ------------------------------------------------------------------------------
# Part 2: Complete subset_word_list function by only keeping words in list up to 
# max_len. Function takes two arguments: a list of words and a maximum length.
# It returns only words that are less than or equal to max_len. 
# When finished, test your code by uncommenting and running test_subset_word_list.
# ------------------------------------------------------------------------------
         
def subset_word_list(list_of_words, max_len):
    """
    Return a list of words containing words up to length max_len from 
    list_of_words. For example, if:

        list_of_words = ["because", "grape", "applesauce", "pink", "groovy"]

    and max_len = 5, the function should return: ["grape", "pink"]

    Parameters
    ----------
    list_of_words: list
        Initial list of words. 

    max_len: int
        The maximum number of characters for retained words.
    
    Returns
    -------
    list
        List of words each having at most length max_len.
    """

    ### TODO ###################################################################
    # - Create a new list to hold words that satisfy the max_len criteria. 
    #
    # - Iterate (loop over) each word in list_of_words, checking if 
    #   the length of the word is less than or equal to max_len. If it is,
    #   append it to the new list you created. 
    #
    # - Return the new list with words having length less than or equal to 
    #   max_len. Replace the empty returned list with your newly created list.
    #
    # - Requires 7-10 LOCs excluding comments. 
    #
    ####################### YOUR CODE HERE #####################################

    if max_len <= 0:

        words = list_of_words
    
    else:
        words = []

        for w in list_of_words:

            if len(w) <= max_len:

                words.append(w)
        
    return words




# ------------------------------------------------------------------------------
# Part 3: Complete the find_substr function. When finished, test your function
# by uncommenting and running `test_find_substr`.
# ------------------------------------------------------------------------------

def find_substr(word_list, substr=None):
    """
    Starting with word_list, find all the words that contain the given 
    substring substr. For example, if substr = "zeb", your function
    should return a list with all  the words from word_list that contain 
    "zeb" (i.e. "zebra", "gazebo", "jezebel", ...).

    Parameters
    ----------
    word_list: list
        List of words. 

    substr: str
        Substring to check.

    Returns
    -------
    list
        A list of all the words from word_list that contain substr. 
    """
    ### TODO ###################################################################
    # - Create a new empty list.
    #
    # - If substr is None (the default), return the original list.
    #
    # - Iterate (loop over) each word in word_list, checking if substr
    #   is found in the word.
    #
    # - If substr is in the word, append it to your new list.
    #
    # - Return the subset of words that match substr. Replace the empty 
    #   returned list with your newly created list.
    #
    # - Requires 8-12 LOCs excluding comments. 
    # 
    ####################### YOUR CODE HERE #####################################

    if substr is None:

        word_list2 = word_list

    else:

        word_list2 = []

        for word in word_list:

            if substr in word:

                word_list2.append(word)

    return word_list2




def main():

    ### TODO ###################################################################
    #
    # - Start by loading the preprocessed word list (hint: Call preprocess function)
    #
    # - Reduce the preprocessed word_list to words having length 15 or less 
    #   (hint: use subset_word_list function).
    #
    # - Get a count of the number of words containing each vowel (a, e, i, o, u).
    #   Process each letter in a for loop, and print the letter, along with 
    #   the number of words containing that letter (hint: use find_substr 
    #   function to find the number of words that contain each letter, then 
    #   find the length of that list). Output for each letter should be (not 
    #   the actual value):
    #
    #               vowel=a, number of occurrences=34,000
    #
    # - Challenge: Include the proportion of words containing the given vowel 
    #   in the print statement. Output should be:
    #
    #               vowel=a, number of occurrences=34000, 13.4% of words contain a.
    #
    # - Requires 
    #
    ####################### YOUR CODE HERE #####################################
    
    vowels = ["a", "e", "i", "o", "u"]

    # Load preprocessed word list.
    word_list_original = preprocess()

    # Subset word_list to words having length 15 or less.
    word_list = subset_word_list(word_list_original, 15)

    nbr_all_words = len(word_list)


    # Iterate over each vowel. Get count of words containing letter.
    for vowel in vowels:

        # Create list of words that contain at least one instance of vowel.
        words_with_vowel = find_substr(word_list, vowel)

        nbr_words = len(words_with_vowel)

        prop_words = nbr_words / nbr_all_words

        print(f"vowel={vowel}, number of occurrences={nbr_words:,}, {prop_words:.2%} words contain {vowel}.")


    # vowel=a, number of occurrences=37,268, 51.27% words contain a.
    # vowel=e, number of occurrences=47,948, 65.96% words contain e.
    # vowel=i, number of occurrences=38,776, 53.34% words contain i.
    # vowel=o, number of occurrences=28,466, 39.16% words contain o.
    # vowel=u, number of occurrences=18,066, 24.85% words contain u.
        
    # Logic to check if a word starts and ends with the same character.
    # 4669

    start_end_same = []
    
    for word in word_list:

        if word[0] == word[-1]:
            start_end_same.append(word)

    print(len(start_end_same))

    



# Function tests ---------------------------------------------------------------


def test_preprocess():
    """
    Test whether output of preprocess function matches expected result.
    """
    print("\nTesting preprocess...")
    expected_len = 72934
    actual_len = len(preprocess())

    
    print(f"Expected length: {expected_len:,}.")
    print(f"Actual length  : {actual_len:,}.")

    if expected_len == actual_len:
        print("preprocess test PASSED.\n")
    else:
        print("preprocess test FAILED.\n")



def test_subset_word_list():
    """
    Test whether output of subset_word_list function matches expected result.
    """
    print("\nTesting subset_word_list...")
    test_words = ["aaaa", "aaaaaaaaaa", "aaaaaaaaa", "aaaaa", "aa", "a", "aaaaaaaaaaaa"]
    expected_len = 4
    actual_len = len(subset_word_list(test_words, 5))

    print(f"Expected length: {expected_len:,}.")
    print(f"Actual length  : {actual_len:,}.")

    if expected_len == actual_len:
        print("subset_word_list test PASSED.\n")
    else:
        print("subset_word_list test FAILED.\n")



def test_find_substr():
    """
    Test whether output of find_substr function matches expected result.
    """
    print("\nTesting find_substr...")

    test_words = ["capital", "captain", "fool", "and", "me", "science", "caps"]
    test_str = "cap"
    expected_len = 3
    actual_len = len(find_substr(test_words, test_str))

    print(f"Expected length: {expected_len:,}.")
    print(f"Actual length  : {actual_len:,}.")

    if expected_len == actual_len:
        print("find_substr test PASSED.\n")
    else:
        print("find_substr test FAILED.\n")




if __name__ == "__main__":

    # test_preprocess()
    # test_find_substr()
    # test_subset_word_list()
    main()

