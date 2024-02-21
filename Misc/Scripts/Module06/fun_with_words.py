"""
Functions to manipulate the Linux words file. Spring 2024 CIS189 Module 6 
in-class project.
"""
import urllib.request



############### DO NOT MODIFY CODE BETWEEN LINES 8 AND 100 #####################


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


################################################################################




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
        List of words in lowercase with whitespace stripped and apostrophes 
        removed. 
    """
    # Load initial words list by calling get_word_list. 
    word_list = get_word_list()

    ### TODO ###################################################################
    # - Create a new empty list for retained words.
    #
    # - Iterate (loop over) each word in word_list, removing whitespace 
    #   (`.strip()`) and converting each to lowercase. (`.lower()`). 
    #
    # - If word contains an apostrophe ('), do not append it to new list.
    #
    # - All remaining words should be appended to new list.
    #
    # - Replace the empty returned list with your newly created list.
    #
    # - Requires 5-8 LOCs (excluding comments). 
    #
    ####################### YOUR CODE HERE #####################################

    return []
    



# ------------------------------------------------------------------------------
# Part 2: Complete subset_word_list function by only keeping words in 
# list_of_words up to max_len. Function takes two arguments: a list of words 
# and a maximum length. It returns only words that are less than or equal to 
# max_len. If max len is less than or equal to 0, original list should be 
# returned. When finished, test your code by running test_subset_word_list.
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
    #   append it to the newly created list.
    #
    # - Return the new list with words having length less than or equal to 
    #   max_len. Replace the empty returned list with your newly created list.
    #
    # - Requires 4-6 LOCs excluding comments. 
    #
    ####################### YOUR CODE HERE #####################################

    return []




# ------------------------------------------------------------------------------
# Part 3: Complete the find_substr function. If substr is None, return input 
# list. When finished, test your function by running `test_find_substr`.
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

    return []




# ------------------------------------------------------------------------------
# Part 4: Complete main function. Uncomment `main()` under if __name__ == "__main__"
# prior to running.
# ------------------------------------------------------------------------------

def main():

    vowels = ["a", "e", "i", "o", "u"]

    ### TODO ###################################################################
    #
    # - Start by loading the preprocessed word list (hint: Call preprocess function)
    #
    # - Reduce the preprocessed word_list to words having length 15 or less 
    #   (hint: use subset_word_list function).
    #
    # - Get a count of the number of words containing each vowel (a, e, i, o, u).
    #   Process each letter in a for loop and print the letter along with 
    #   the number of words containing that letter (hint: use find_substr 
    #   function to find the number of words that contain each letter, then 
    #   find the length of that list and print it). Output for each letter 
    #   should be something like:
    #
    #               vowel=a, number of occurrences=100
    #
    # - Challenge: Include the proportion of words containing the given vowel 
    #   in the print statement to 2 decimal places. Output should be:
    #
    #               vowel=a, number of occurrences=34000, 13.40% of words contain a.
    #
    #
    # - Requires 7-10 LOCs excluding comments.
    #
    # - Challenge requires only 2 additional LOCs and a modified print statement.
    #
    ####################### YOUR CODE HERE #####################################
    

    # Load preprocessed word list (hint: call preprocess function, assign it to a variable).
    


    # Subset word_list to words having length 15 or less (hint: call subset_word_list function).



    # Iterate over vowels list (defined above). Get count of words containing letter and 
    # print the vowel along with the number of occurrences.


    # Challenge #2: Print the number of words in original preprocessed word list
    # that start and end with the same character.











if __name__ == "__main__":
    
    test_preprocess()
    test_find_substr()
    test_subset_word_list()
    # main()

