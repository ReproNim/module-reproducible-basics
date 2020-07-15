* `questions.xml` - the xml file with all the questions (the file was created from the txt file using python script `quizzes_xml.py`)


* `questions.txt` - contains all the questions, using format:

      qst| What is your question?

      A| your answer A

      B| your answer B

      C| your answer C

      D| your answer D

      Answer| correct answers, e.g. "a, c"

      type| "multi" (or "single", optional the default is "single" if one answer provided, and "multi" otherwise)

* `quizzes_xml.py` - python script that converts txt file to xml using the moodle spec.
