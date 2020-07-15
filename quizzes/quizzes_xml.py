import string
import xml.etree.ElementTree as ET
from xml.dom import minidom
from pathlib import Path


TYPES = ["single", "multi", "truefalse"]

def validate_quiz(quiz, it):
    quiz.setdefault("name", f"Question {it}")
    if "answer" not in quiz.keys():
        raise Exception("answer has to be provided")
    if "qst" not in quiz.keys():
        raise Exception("question has to be provided")

    if "type" in quiz:
        if quiz["type"] == "single":
            if len(quiz["answer"]) != 1 or quiz["answer"][0] not in quiz:
                raise Exception("answer for a single type has to be single and must be a valid key")
            else:
                quiz["answer"] = quiz["answer"][0]
        elif quiz["type"] == "multi":
            for el in quiz["answer"]:
                if el not in quiz.keys():
                    raise Exception(f"answer {el} is not provided")
        elif quiz["type"] == "truefalse":
            quiz["answer"] = quiz["answer"][0]
            if quiz["answer"] not in ["true", "false"]:
                raise Exception(f"answer for truefalse qst has to be true or false,"
                                f" but {quiz['answer']} provided")
        else:
            raise Exception(f"quiz type has to be in {TYPES}")
    else: # guessing the type
        if len(quiz["answer"]) > 1:
            for el in quiz["answer"]:
                if el not in quiz.keys():
                    raise Exception(f"answer {el} is not provided")
            quiz["type"] = "multi"
        elif quiz["answer"][0] in ["true", "false"]:
            quiz["answer"] = quiz["answer"][0]
            quiz["type"] = "truefalse"
        else:
            quiz["answer"] = quiz["answer"][0]
            if quiz["answer"] not in quiz:
                raise Exception("answer has to be a valid key")
            quiz["type"] = "single"
    return quiz


def read_qstfile(filename):
    quizzes_list = []
    with open(filename) as f:
        quiz = {}
        for el in f.readlines():
            if el.startswith("##") and quiz:
                quiz = validate_quiz(quiz, it=len(quizzes_list)+1)
                quizzes_list.append(quiz)
                quiz = {}
            elif el.strip() == "":
                continue
            else:
                print("el", el)
                if len(el.split("|")) != 2:
                    raise Exception(f"error in the line: {el}")
                key, val = el.split("|")
                key, val = key.lower().strip(), val.strip()
                if key in ["qst", "question", "qst."]:
                    quiz["qst"] = val
                elif key in ["ans", "ans.", "answer"]:
                    quiz["answer"] = [v.lower().strip() for v in val.split(',')]
                elif key in ["type", "tp", "tp."]:
                    val = val.lower()
                    if val in TYPES:
                        quiz["type"] = val
                elif key in ["name", "nm", "nm."]:
                    quiz["name"] = val
                elif len(key) == 1 and key in string.ascii_lowercase:
                    quiz[key] = val
                else:
                    raise Exception(f"not valid key provided - {key}")

        if quiz:
            quiz = validate_quiz(quiz, it=len(quizzes_list) + 1)
            quizzes_list.append(quiz)

    return quizzes_list


def xml_create(quizzes_list, namefile="questions.xml"):
    quiz_root = ET.Element('quiz')
    qst = ET.SubElement(quiz_root, 'qstiii')
    qst.text = 'This child contains text.'

    qst = ET.SubElement(quiz_root, 'qst')
    qst.text = 'another child contains text.'

    for quiz_dict in quizzes_list:
        type = quiz_dict.pop("type")
        if type == "single":
            add_single(quiz_dict, quiz_root)
        elif type == "multi":
            add_multi(quiz_dict, quiz_root)
        elif type == "truefalse":
            raise Exception("truefalse not implemented")

    quiz_reparsed = minidom.parseString(ET.tostring(quiz_root)).toprettyxml(indent="  ")#, encoding='UTF-8')
    quiz_reparsed = quiz_reparsed.replace("</question>", "</question>\n")

    with open(namefile, "w") as f:
        f.write(quiz_reparsed)



def add_single(question, quiz):
    correct_ans = question.pop("answer")
    qst = ET.SubElement(quiz, 'question')
    qst.set("type", "multichoice")
    qsttext = ET.SubElement(qst, 'questiontext')
    qsttext.set("format", "html")
    qsttext_txt = ET.SubElement(qsttext, 'text')
    qsttext_txt.text = question.pop("qst")
    name = ET.SubElement(qst, 'name')
    name_txt = ET.SubElement(name, 'text')
    name_txt.text = question.pop("name")
    type = ET.SubElement(qst, 'single')
    type.text = "true"

    for ans_el in sorted(question):
        if ans_el in string.ascii_lowercase:
            ans = ET.SubElement(qst, 'answer')
            ans_txt = ET.SubElement(ans, 'text')
            ans_txt.text = question.pop(ans_el)
            fdb = ET.SubElement(ans, 'feedback')
            fdb_txt = ET.SubElement(fdb, 'text')
            if ans_el == correct_ans:
                ans.set("fraction", "100")
                fdb_txt.text = 'Correct answer!'
            else:
                ans.set("fraction", "0")
                fdb_txt.text = 'Wrong answer'
    if question:
        raise Exception(f"question has too many elements, {question} is left")


def add_multi(question, quiz):
    correct_ans_l = question.pop("answer")
    correct_frac_l = [100 // len(correct_ans_l)
                      if ii >= 100 % len(correct_ans_l) else 100 // len(correct_ans_l) + 1
                      for (ii, el) in enumerate(correct_ans_l)]
    qst = ET.SubElement(quiz, 'question')
    qst.set("type", "multichoice")
    qsttext = ET.SubElement(qst, 'questiontext')
    qsttext.set("format", "html")
    qsttext_txt = ET.SubElement(qsttext, 'text')
    qsttext_txt.text = question.pop("qst")
    name = ET.SubElement(qst, 'name')
    name_txt = ET.SubElement(name, 'text')
    name_txt.text = question.pop("name")
    type = ET.SubElement(qst, 'single')
    type.text = "false"

    for ans_el in sorted(question):
        if ans_el in string.ascii_lowercase:
            ans = ET.SubElement(qst, 'answer')
            ans_txt = ET.SubElement(ans, 'text')
            ans_txt.text = question.pop(ans_el)
            fdb = ET.SubElement(ans, 'feedback')
            fdb_txt = ET.SubElement(fdb, 'text')
            if ans_el in correct_ans_l:
                ans.set("fraction", str(correct_frac_l.pop()))
                fdb_txt.text = 'Correct answer!'
            else:
                ans.set("fraction", "0")
                fdb_txt.text = 'Wrong answer'
    if question:
        raise Exception(f"question has too many elements, {question} is left")


def convert_txt_to_xml(filename_txt="questions.txt", filename_xml="questions.xml"):
    path_txt = Path(__file__).parent.absolute() / filename_txt
    path_xml = Path(__file__).parent.absolute() / filename_xml

    quizzes = read_qstfile(path_txt)
    xml_create(quizzes, path_xml)


convert_txt_to_xml()

