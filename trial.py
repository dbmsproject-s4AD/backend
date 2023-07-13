import MySQLdb
import os
from dotenv import load_dotenv
load_dotenv()

# print(os.getenv("PASSWORD"))
# print(os.getenv("HOST"))
print(os.getenv("USER"))
# print(os.getenv("DATABASE"))

connection = MySQLdb.connect(
    host=os.getenv("HOST"),
    user=os.getenv("USER"),
    passwd=os.getenv("PASSWORD"),
    db=os.getenv("DATABASE"),
    autocommit=True,
    ssl_mode="VERIFY_IDENTITY",
    ssl={
        "ca": "./cacert.pem"
    }
)

print(connection)
connection.close()
