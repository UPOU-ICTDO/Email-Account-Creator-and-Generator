import sqlite3
import pandas as pd
import logging

# Setup logging config
logging.basicConfig(
    level = logging.DEBUG,
    format = "[{asctime}] {levelname:<8} | {message}",
    style = "{",
    filename = "import-existing-user-script-logs.txt",
    filemode = 'a'
)

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
    	conn = sqlite3.connect(db_file)
    	c = conn.cursor()
    	c.execute('''CREATE TABLE IF NOT EXISTS UPMailAccounts(
        	userid TEXT PRIMARY KEY, 
        	firstname TEXT, 
        	lastname TEXT, 
        	orgUnitPath TEXT,
        	suspended TEXT,
        	lastLoginTime TEXT
        )''')
    except Error as e:
    	print(e)
    return conn

def insert_account(conn, account):
    sql = ''' INSERT OR REPLACE INTO UPMailAccounts(userid, firstname, lastname, orgUnitPath, suspended, lastLoginTime)
              VALUES(?, ?, ?, ?, ?, ?) '''

    cur = conn.cursor()
    cur.execute(sql, account)
    conn.commit()
    return cur.lastrowid

def main(csv_to_read):
    #read CSV then insert to database
    # CHANGE SOURCE OF FILE TO THE ONE INPUTTED BY THE USER FROM THE GUI - 'NewUPGoogleUsers.csv'
    df = pd.read_csv(csv_to_read, usecols=['First Name [Required]', 'Last Name [Required]', 'Org Unit Path [Required]', 'Email Address [Required]', 'Status [READ ONLY]', 'Last Sign In [READ ONLY]'])
    logging.info(f"Imported file from: {csv_to_read}")
    df = df.rename(columns = {'First Name [Required]': 'firstname', 'Last Name [Required]': 'lastname', 'Email Address [Required]': 'userid', 'Org Unit Path [Required]':'orgUnitPath', 'Status [READ ONLY]':'suspended', 'Last Sign In [READ ONLY]':'lastLoginTime'})

    conn = create_connection('gapps.db')
    with conn:
        for i in range(len(df)):
            if (df.loc[i, 'userid'].find("@up.edu.ph") != -1):
                suspended = str(df.loc[i,'suspended'])
                account = (df.loc[i,'userid'], df.loc[i,'firstname'], df.loc[i,'lastname'], df.loc[i,'orgUnitPath'], suspended, df.loc[i,'lastLoginTime'])
                logging.info(f"Imported Account: {account[0]} - {account[1]} {account[2]}")
                insert_account(conn, account)


if __name__ == '__main__':
    main()