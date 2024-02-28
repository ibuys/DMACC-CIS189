"""
CIS189 Module 7 File I/O Assignment.
"""

# ------------------------------------------------------------------------------
# Part 1.: Complete write_to_file function (void).
# ------------------------------------------------------------------------------

def write_to_file(scores, name="some-student-name"):
     """
     Parameters
     ----------
     scores: list
         List of scores.
     name: str
         Student name.
     """
     ##### YOUR CODE HERE #####




# ------------------------------------------------------------------------------
# Part 2: Complete get_student_info function (void).
# ------------------------------------------------------------------------------
     
def get_student_info():
    """
    Put docstring here.
    """
    # Create empty list to hold scores.
    ##### YOUR CODE HERE ######

    # Prompt for student name.
    ##### YOUR CODE HERE ######

    # Prompt for number of scores to enter.
    nbr_scores = int(input("How many scores do you wish to enter? "))

    # Iterate up to nbr_scores, prompting user to enter a score each time.
    for i in range(nbr_scores):

        # Prompt for score.
        ##### YOUR CODE HERE #####

        # Append score to scores list initialized above.
        ##### YOUR CODE HERE #####

    # Pass student scores and name to write_to_file function.
    ##### YOUR CODE HERE #####



# ------------------------------------------------------------------------------
# Part 3: Complete read_from_file function (fruitful).
# ------------------------------------------------------------------------------

def read_from_file(filename):
    """
    Load scores from filename and return string containing filename,
    min score, max score and average score.

    Parameters
    ----------
    filename: str
        Name of file with scores, assumed to have .txt extension.

    Returns
    -------
    str
        String containing filename, min score, max score and average score.
    """
    # Open filename for reading. Load scores into list performing necessary
    # type conversions.
    ##### YOUR CODE HERE #####

    # Identify min, max and average score from list of scores.
    ##### YOUR CODE HERE #####

    # Return string formatted as {filename}: min={min_score}, max={max_score} avg={avg_score}
    ##### YOUR CODE HERE #####

    # Replace pass with your return string.
    pass



if __name__ == "__main___":

    # Call get_student_info for 3 students.
    ##### YOUR CODE HERE #####

    # Call read_from_file for created text files and print the results.
    ##### YOUR CODE HERE #####

    # Remove pass upon completion.
    pass
