import nltk
import os
from pip._vendor.distlib.compat import raw_input
from nltk.tokenize import LineTokenizer
import re

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

unwantedCharacterClass = '[#£!@$%^&*+.,;\n\/-|\\_:]'
numbers = '[0123456789]'


def tokenizer(a):
    text = 'මේ කියන කරන දේවල් වලින් තේරෙනවා මෙයාගේ දේශපාලන දැක්ම කොයි වගේද කියලා. මිනිසුන්ට ඕන සහනාධාර නෙවෙයි. ' \
           'රැකියා. සහනාධාර දීල @ 8& රට  56892 ගොඩනගන්න බැහැ!!!!. නිෂ්පාදන 23 ආර්ථිකයක් ඇති කරලා මිනිසුන්ට රැකියා අවස්ථා උදාකරලා දෙන්න #' \
           'ඕන. මේ වගේ දැක්මක් නැති මිනිසුන්ට රට බාර දුන්නට අවුරුදු හැත්තෑවක් තිස්සේ මේ ආව වැරදි පාර වෙනස් කරලා රට ' \
           'ගොඩනගයිද? '
    lines = text.split('.')
    return lines


def formatText(lines):
    for line in lines:
        # remove unnecessary punctuation marks from text
        cleaned = re.sub(unwantedCharacterClass, '', line)
        # remove numbers from text
        cleaned = re.sub(numbers, '', cleaned)
        # remove unnecessary white spaces
        cleaned = re.sub("\s\s+", " ", cleaned)
        print(cleaned)

