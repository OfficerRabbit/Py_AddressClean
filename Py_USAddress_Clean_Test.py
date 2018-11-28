# Import, pay yer tariffs!
import pypyodbc
import json
import usaddress
from pprint import pprint

# Opening Connection
print("< Opening Connection >")

connection = pypyodbc.connect(r'Driver={SQL Server};'
                              r'Server=SCFSQL01;'
                              r'Database=SummarizedReportData;'
                              r'Trusted_Connection=yes;')

print("\n")

# Show connection info
print("< Connection Information>")								
print(connection)								
print("\n")

# Query info
cursor = connection.cursor()
SQLCommand = ("""
    SELECT-- TOP 100
        PERSON_SK
    ,	ADDRESS_LINE_1
    ,	CITY
    ,	STATE
    ,	POSTAL_CODE = LEFT(Postal_Code, 5)
    FROM
	SummarizedReportData.dbo.CUST_PT_PIV_Demgraf
    WHERE
        Empaneled = 1
    ;
    """)
Values = [2]
cursor.execute(SQLCommand)#, Values)
results = cursor.fetchone()

count = 0
# Print query results
print("< Query Results >")
while results:
    col_person_sk = str(results[0])
    col_address_1 = str(results[1])
    col_city = str(results[2])
    col_state = str(results[3])
    col_zip = str(results[4])
    address_list = [col_address_1, col_city, col_state, col_zip]
    space = " "
    col_full_address = space.join(address_list).replace("None", "").replace("  ", " ")

    print("Person_SK: ", col_person_sk, " Address: ", col_full_address)

    try:
        split_address = usaddress.tag(col_full_address)
        pprint(split_address, indent = 2)
    except usaddress.RepeatedLabelError:
        print("< Record has a repitition of label >")

    count += 1
    print(count)
    results = cursor.fetchone()
