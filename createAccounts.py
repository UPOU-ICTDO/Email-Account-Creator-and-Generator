import sqlite3
import pandas as pd
import numpy as np
import random
import string
import logging

# Setup logging config
logging.basicConfig(
    level = logging.DEBUG,
    format = "[{asctime}] {levelname:<8} | {message}",
    style = "{",
    filename = "create-accounts-script-logs.txt",
    filemode = 'a'
)

new_student_records = []

def generate_password():
    #define data
    length = 9

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits

    #string.ascii_letters

    #combine the data
    all = lower + upper + num

    #use random 
    temp = random.sample(all,length)

    #create the password 
    password = "".join(temp)
    password = password + "!"

    return password

def format_name(name):
    name = name.lower()
    name = name.strip()
    name = name.replace('ñ', 'n')
    name = name.replace('.', '')
    name = name.replace(',', '')
    name = name.replace("'", "")
    name = name.replace("`", "")

    return name.title()

def generate_user_id(lastname, firstname, middlename):
    userid = ""

    if ( len(middlename) > 0 ):
        userid = str(firstname[0]) + str(middlename[0]) + str(lastname)
    else:
        userid = str(firstname[0]) + str(lastname)

    userid = userid.replace('-', '')
    userid = userid.replace(' ', '')

    return userid.lower()

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def create_table(conn):
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS UPOUAccounts(
        userid TEXT PRIMARY KEY, 
        firstname TEXT, 
        lastname TEXT, 
        orgUnitPath TEXT,
        suspended TEXT,
        lastLoginTime TEXT,
        studno TEXT,
        email TEXT,
        status TEXT,
        tempPassword TEXT
    )''')

def insert_account(conn, account):
    sql = ''' INSERT INTO UPOUAccounts(userid, firstname, lastname, orgUnitPath, suspended, lastLoginTime, studno, email, status, tempPassword)
        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?) '''
    try:
        cur = conn.cursor()
        cur.execute(sql, account)
        conn.commit()
        return cur.lastrowid
    except:
        return None


def account_exists(conn, firstname, lastname, temp_userid, studno, email):
    cur = conn.cursor()
    status = "old"
    temp_password = ""
    uid = temp_userid + '%'

    cur.execute("SELECT * FROM UPMailAccounts WHERE firstname=? AND lastname=? AND userid LIKE ?", (firstname, lastname, uid ))

    rows = cur.fetchall()

    if len(rows) > 0:
        for row in rows:
            # 0 - userid, 1 - firstname, 2 - lastname, 3 - orgUnitPath, 4 - suspended, 5 - lastLoginTime
            if (str(row[5]) == "Never"):
                temp_password = generate_password()
                
            account = (row[0], row[1], row[2], row[3], row[4], row[5], studno, email, status, temp_password)
            insert_account(conn, account)
        return True
    else:
        return False

def create_new_account(conn, firstname, lastname, temp_userid, studno, email, status):

    cur = conn.cursor()
    uid = temp_userid + '%'
    orgUnitPath = "/Students/UP Open University Students/Active UPOU Students"

    cur.execute("SELECT userid FROM UPMailAccounts WHERE userid LIKE ?", (uid,))
    rows = cur.fetchall()
    suspended = "False"

    userid = temp_userid
    nums = []

    for row in rows:
        temp = row[0].replace("@up.edu.ph", "")
        num = temp.replace(temp_userid, "") 
        
        if num.isnumeric():
            nums.append(int(num))
        elif num == "":
            nums.append(0)

    if len(nums) > 0:
        userid = temp_userid + str(max(nums) + 1) 

    userid = userid + "@up.edu.ph"
    print( temp_userid, userid, nums )

    temp_password = generate_password()
    last_login = ""

    account = (userid, firstname, lastname, orgUnitPath, suspended, last_login, studno, email, status, temp_password)
    
    #email address,first name,last name,org unit path,Recovery Email,password
    
    
    curr_dict = {}
    curr_dict["email address"] = userid
    curr_dict["first name"] = firstname
    curr_dict["last name"] = lastname
    curr_dict["org unit path"] = orgUnitPath
    #curr_dict[] = suspended
    #curr_dict[] = last_login
    #curr_dict[] = studno
    curr_dict["Recovery Email"] = email
    #curr_dict[] = status
    curr_dict["password"] = temp_password
    
    new_student_records.append(curr_dict)
    
    insert_account(conn, account)


def main(csv_to_read):
    conn = create_connection('gapps.db')
    create_table(conn)
    ctr = 1

    #read CSV then insert to database
    # Change pdf source 
    df = pd.read_csv(csv_to_read, sep = ';', usecols=['email', 'lastname', 'firstname', 'middlename', 'idnumber'])
    df = df.rename(columns = {'idnumber': 'studentno'})
    df = df.fillna('')

    with conn:
        for i in range(len(df)):

            if (df.loc[i,'lastname'].find(" JR") != -1):
                lastname = format_name(df.loc[i,'lastname'].replace(" JR", ""))
                firstname = format_name(df.loc[i,'firstname'].strip() + " JR")
            elif (df.loc[i,'lastname'].find(" III") != -1):
                lastname = format_name(df.loc[i,'lastname'].replace(" III", ""))
                firstname = format_name(df.loc[i,'firstname'].strip() + " III")
            else:
                lastname = format_name(df.loc[i,'lastname'])
                firstname = format_name(df.loc[i,'firstname'])

            middlename = format_name(df.loc[i,'middlename'])

            studno = df.loc[i,'studentno']
            batch = int(studno[0:4])

            temp_userid = generate_user_id(lastname, firstname, df.loc[i,'middlename'])

            if account_exists(conn, firstname, lastname, temp_userid, df.loc[i,'studentno'], df.loc[i,'email']) == False:
                if (batch == 2021 or batch < 2000):
                    status = "new"
                    logging.info(f"Created account: {firstname} {lastname} - STATUS: NEW")
                    create_new_account(conn, firstname, lastname, temp_userid, df.loc[i,'studentno'], df.loc[i,'email'], status)
                else :
                    status = "check"
                    logging.info(f"Created account: {firstname} {lastname} - STATUS: CHECK")
                    create_new_account(conn, firstname, lastname, temp_userid, df.loc[i,'studentno'], df.loc[i,'email'], status)
            else:
                print (ctr, "Existing: ", lastname, ", ", firstname)
                ctr += 1

    new_stud_df = pd.DataFrame(new_student_records)
    #print (new_stud_df)
    #display (new_stud_df)

    # Generated csv to be viewed later
    logging.info(f"File saved to RV_new_uploads.csv")
    new_stud_df.to_csv("RV_new_uploads.csv", index=False)


if __name__ == '__main__':
    main()