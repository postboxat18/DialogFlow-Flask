
from firebase import firebase
firebase = firebase.FirebaseApplication('https://pythonmysql-db11a-default-rtdb.firebaseio.com/', None)
data =  { 'Name': 'John Doe',
          'RollNo': 3,
          'Percentage': 70.02
          }
result = firebase.post('/pythonmysql-db11a-default-rtdb/Students/',data)
print(result)