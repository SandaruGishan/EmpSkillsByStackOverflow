import requests
import json
import demjson
import parser
import mysql.connector
import psycopg2



from mysql.connector import Error
a = 157247
response = requests.get("https://api.stackexchange.com//2.2/users/"+str(a)+"?order=desc&sort=reputation&site=stackoverflow")


def connect(userName,userId,reputation,goldBadgeCount,siverBadgeCount,bronzeBadgeCount,acceptRate,lastActivateDate,stackId):
    """
    connect to MySQL database and insert twitter data
    """
    try:
        con = psycopg2.connect(host='localhost', database='EmpSkill', user='postgres', password='abcd', 
                                      )

        if (con):

            cursor = con.cursor()
            # twitter, golf
            query          = "INSERT INTO users (userName,userId,reputation,goldBadgeCount,silverBadgeCount,bronzeBadgeCount,acceptRate,lastActivateDate,stackId) VALUES (%s, %s, %s, %s, %s, %s,%s, %s, %s)"
            cursor.execute(query, (userName,userId,reputation,goldBadgeCount,siverBadgeCount,bronzeBadgeCount,acceptRate,lastActivateDate,stackId))
            con.commit()



    except Error as e:
        print(e)



    return











def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

udata=response.json()

raw_data = json.loads(response.text)

rpt = raw_data['items']
for items in rpt:
 userName=items['display_name']
 reputation = items['reputation']
 goldBadgeCount = 5
 siverBadgeCount =5
 bronzeBadgeCount = 8
 acceptRate = 23
 lastActivateDate =  '10032019'
 stackId = 157247
 userId=0

 connect(userName,userId,reputation,goldBadgeCount,siverBadgeCount,bronzeBadgeCount,acceptRate,lastActivateDate,stackId)
jprint(userName)


"""""
jprint(rpt)
def on_data(self, udata):
    try:
        raw_data = json.loads(udata)

        if 'text' in raw_data:

            username = raw_data['items']['accept_rate']
            created_at = parser.parse(raw_data['created_at'])
            tweet = raw_data['text']
            retweet_count = raw_data['retweet_count']
            rpt = raw_data['reputation']
            jprint(username)

            jprint(rpt)5
            if raw_data['place'] is not None:
                place = raw_data['place']['country']
                print(place)

            else:
                place = None

            location = raw_data['user']['location']

            # insert data just collected into MySQL database
            connect(username, created_at, tweet, retweet_count, place, location)
            print("Tweet colleted at: {} ".format(str(created_at)))
    except Error as e:
        print(e)
#jprint(udata)

"""""