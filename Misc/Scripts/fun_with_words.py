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
        3. Remove any words with single quote (apostrophe).

    Returns
    -------
    list
        List of words with length greater than three, less than 15 in lowercase
        with apostrophes removed. 
    """
    # Load initial words list by calling get_word_list. 
    word_list = get_word_list()

    ### TODO ###################################################################
    # - Create a new empty list named word_list2. 
    #
    # - Iterate (loop over) each word in word_list, removing whitespace 
    #   (`.strip()`) and converting to lowercase. (`.lower()`). 
    #
    # - If word contains an apostrophe ('), do not append it to word_list2. 
    #
    # - All remaining words should be appended to word_list2. 
    #
    # - Replace the empty list return with word_list2. 
    #
    # - Should be no more than 5-10 LOCs. 
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
# Part 2: Complete the find_substr function. When finished, test your function
# by uncommenting and running `test_find_substr`.
# ------------------------------------------------------------------------------

def find_substr(word_list, substr):
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
    # - Create a new empty list named word_list2. 
    #
    # - Iterate (loop over) each word in word_list, checking if substr
    #   is found in the word.
    #
    # - If substr is in the word, append it to word_list2. 
    #
    # - Return the subset of words that match substr. 
    #
    # - Should be no more than 5-8 LOCs. 
    # 
    ####################### YOUR CODE HERE #####################################
    word_list2 = []

    for word in word_list:

        if substr in word:

            word_list2.append(word)

    return word_list2






# ------------------------------------------------------------------------------
# Part 3: Complete subset_words function, by only keeping words in list up to 
# max_len. Function takes two arguments: a list of words and a maximum length.
# It returns only words that are less than or equal to max_len. 
# ------------------------------------------------------------------------------
         
def subset_words(list_of_words, max_len):
    """
    Return a word list containing words up to length max_len from 
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
    # - Return the new list with words having length less than max_len.
    #
    # - Should be no more than 4-6 LOCs.
    #
    ############################################################################
    words = []

    for w in list_of_words:

        if len(w) <= max_len:

            words.append(w)
        
    return words







# Development area -------------------------------------------------------------

all_words = preprocess()













# Function tests ---------------------------------------------------------------

def test_preprocess():
    """
    Test whether output of preprocess function matches expected result.
    """
    expected_len = 72934
    actual_len = len(preprocess())

    print("Testing preprocess...")
    print(f"Expected length: {expected_len:,}.")
    print(f"Actual length  : {actual_len:,}.")

    if expected_len == actual_len:
        print("preprocess test PASSED.\n")
    else:
        print("preprocess test FAILED.\n")



def test_find_substr():
    """
    Test whether output of find_substr function matches expected result.
    """
    test_str = "cap"
    expected_len = 208
    actual_len = len(find_substr(test_str))

    print("Testing find_substr...")
    print(f"Expected length: {expected_len:,}.")
    print(f"Actual length  : {actual_len:,}.")

    if expected_len == actual_len:
        print("find_substr test PASSED.\n")
    else:
        print("find_substr test FAILED.\n")



test_preprocess()
test_find_substr()

