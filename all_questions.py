"""
Work with DENCLUE clustering.
Do not use global variables!
"""

import pickle
from typing import Any

import matplotlib.pyplot as plt
from numpy.typing import NDArray


######################################################################
#####     CHECK THE PARAMETERS     ########
######################################################################


def question1() -> dict:
    """Answer question 1."""

    answers = {}

    # There is no question 1. Skip.

    return answers


# ----------------------------------------------------------------------
def question2() -> dict:
    """Answer question 2."""

    answers = {}

    answers["q2_1"] = ["discrete", "ratio", "quantitative"]
    answers["q2_2"] = ["continuous", "ratio", "quantitative"]
    answers["q2_3"] = ["continuous", "interval", "quantitative"]
    answers["q2_4"] = ["discrete", "ordinal", "qualitative"]
    answers["q2_5"] = ["discrete", "nominal", "qualitative"]

    return answers


# ----------------------------------------------------------------------
def question3() -> dict:
    """Answer question 3."""

    answers = {}

    answers["q3_1"] = {"discrete", "quantitative", "ratio"}
    answers["q3_2"] = {"discrete", "qualitative", "ordinal"}
    answers["q3_3"] = {"discrete", "qualitative", "ordinal"}
    answers["q3_4"] = {"continuous", "quantitative", "ratio"}
    answers["q3_5"] = {"discrete", "qualitative", "nominal"}
    answers["q3_6"] = {"continuous", "quantitative", "ratio"}
    answers["q3_7"] = {"discrete", "qualitative", "nominal"}
    answers["q3_8"] = {"discrete", "qualitative", "ordinal"}

    return answers


# ----------------------------------------------------------------------
def question4() -> dict:
    """Answer question 4."""

    answers = {}

    answers["q4_1"] = ["nominal", "nominal"]
    answers["q4_2"] = ["ratio", "ordinal"]
    answers["q4_3"] = ["ratio", "ordinal"]
    answers["q4_4"] = ["ratio", "ordinal"]
    answers["q4_5"] = ["ratio", "ratio"]
    answers["q4_6"] = ["ratio", "ordinal"]
    answers["q4_7"] = ["ratio", "interval"]
    answers["q4_8"] = ["ratio", "interval"]

    return answers


# ----------------------------------------------------------------------
def question5() -> dict:
    """Answer question 5."""

    answers = {}

    answers["q5_1"] = {"bin1": [1, 2, 3, 4, 5], "bin2": [6, 7, 8], "bin3": [9]}
    answers["q5_2"] = {"bin1": [1, 2, 3], "bin2": [4, 5, 6], "bin3": [7, 8, 9]}
    answers["q5_3"] = {"bin1": [1, 2, 3, 4], "bin2": [5, 6, 7], "bin3": [8, 9]}
    answers["q5_4"] = None

    return answers


# ----------------------------------------------------------------------
def question6() -> dict:
    """Answer question 6."""

    answers = {}

    answers["q6_1"] = {"equal_width": ["No Change"], "equal_freq": ["No change"]}
    answers["q6_2"] = {"equal_width": ["No Change"], "equal_freq": ["No change"]}
    answers["q6_3"] = {"equal_width": ["Change is"], "equal_freq": ["No change"]}

    return answers


# ----------------------------------------------------------------------
def question7() -> dict:
    """Answer question 7."""

    answers = {}

    answers["q7_1"] = "increase/decrease"
    answers["q7_2"] = "non-increasing"
    answers["q7_3"] = [(0.0, 2.0), (3.0, 4.0), (5.0, 6.0), (7.0, 100.0)]

    return answers


# ----------------------------------------------------------------------
def question8() -> dict[str, Any]:
    """Answer question 8."""

    answers = {}

    answers["q8_1"] = ["x1", "x2"]
    answers["q8_2"] = "equally similar"
    answers["q8_3"] = "equally similar"
    answers["q8_4"] = ["x2", "y3"]

    return answers


# ----------------------------------------------------------------------
def question9() -> dict[str, Any]:
    """Answer question 9."""

    answers = {}

    answers["q9_1"] = "SMC"
    answers["q9_1_explain"] = "Simple Matching Coefficient is ideal for True/False exam answers because both types of matches (True-True and False-False) contribute equally to the similarity score."

    answers["q9_2"] = "Jaccard"
    answers["q9_2_explain"] = "Jaccard is ideal for location visit data because it only counts shared visits (yes-yes matches) and excludes shared non-visits (no-no matches), which are uninformative for measuring similarity."

    answers["q9_3"] = "Correlation"
    answers["q9_3_explain"] = "Correlation is ideal for network traffic flows because it measures pattern similarity independent of magnitude, whereas Euclidean distance is sensitive to scale differences."

    answers["q9_4"] = "Euclidean"
    answers["q9_4_explain"] = "Euclidean distance is ideal for comparing coordinates in 2D space because it directly measures the geometric distance between points."

    answers["q9_5"] = "Cosine Similarity"
    answers["q9_5_explain"] = "Cosine similarity is ideal for binary purchase vectors because it measures pattern similarity independent of magnitude, focusing only on which items were bought regardless of the total quantity."

    return answers


# ----------------------------------------------------------------------
def question10() -> dict:
    """Answer question 10."""

    answers = {}

    answers["q10_1"] = False
    answers["q10_1_explain"] = "Random fluctuations in count data can introduce noise that distorts observed frequencies and patterns."

    answers["q10_2"] = True
    answers["q10_2_explain"] = "The correlation coefficient for any two real-valued vectors always falls within the range of -1 to 1."

    answers["q10_3"] = False
    answers["q10_3_explain"] = "Aggregation preserves more information about trends and patterns than sampling, which may lose important data points."

    answers["q10_4"] = True
    answers["q10_4_explain"] = "While some outliers are noise, others represent legitimate but rare observations in the data."

    answers["q10_5"] = False
    answers["q10_5_explain"] = "Outliers are not always noise; they can represent legitimate but infrequent events in the data."

    answers["q10_6"] = False
    answers["q10_6_explain"] = "Binary attributes are only asymmetric if one value is more informative than the other; not all binary attributes have this property."

    answers["q10_7"] = False
    answers["q10_7_explain"] = "Cosine similarity of 1 indicates vectors point in the same direction but can have different magnitudes."

    answers["q10_8"] = False
    answers["q10_8_explain"] = "Discrete count variables can be ratio-scaled if they have a zero point and equal intervals."

    answers["q10_9"] = False
    answers["q10_9_explain"] = "Quantitative variables can be either continuous or discrete; not all are continuous."

    answers["q10_10"] = False
    answers["q10_10_explain"] = "Converting ordinal variables to asymmetric binary variables loses the ordering information in the original data."

    return answers


# ----------------------------------------------------------------------
if __name__ == "__main__":
    answers_dict = {}

    function_names = ["question" + str(i) for i in range(1, 11)]

    for name in function_names:
        answers_dict[name] = globals()[name]()

    with open("all_questions.pkl", "wb") as fd:
        pickle.dump(answers_dict, fd, protocol=pickle.HIGHEST_PROTOCOL)
