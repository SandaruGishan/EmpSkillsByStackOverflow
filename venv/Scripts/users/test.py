import psycopg2
import nltk
import os
from pip._vendor.distlib.compat import raw_input
from nltk.tokenize import LineTokenizer
import re

unwantedCharacterClass = '[#£!@$%^&*+.,;\n\/-|\\_:]'
numbers = '[0123456789]'


def tokenizer(a):
    text = a
    lines = text.split('.')
    formatText(lines)
    print(lines)
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


try:
    connection = psycopg2.connect(user="postgres",
                                  password="abcd",
                                  database="EmpSkill")

    print("Selecting rows from mobile table using cursor.fetchall")
    cursor = connection.cursor()
    postgreSQL_select_Query = "select * from comments"

    cursor.execute(postgreSQL_select_Query)
    mobile_records = cursor.fetchmany(20)

    print("Printing 2 rows")
    for row in mobile_records:
        print(" = ", row[0], )
        print(" = ", row[1])
        print(" = ", row[2])
        print("  = ", row[3], "\n")
    tokenizer(row[1])
    formatText(lines)
    mobile_records = cursor.fetchmany(2)


except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)

finally:
    # closing database connection.
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))



