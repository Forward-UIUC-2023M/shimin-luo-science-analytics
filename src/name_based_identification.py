# Two name-based method to identify gender
import requests
import json
import re
import gender_guesser.detector as gender

# method 1: Ethnea
def Ethnea(firstname, lastname):
    print("Method 1: Ethnea")
    # url = "http://abel.lis.illinois.edu/cgi-bin/ethnea/search.py?Fname=Peter&Lname=Bock&format=json"
    url = "http://abel.lis.illinois.edu/cgi-bin/ethnea/search.py?Fname=" + firstname + "&Lname=" + lastname + "&format=json"

    response = requests.get(url)

    if response.status_code == 200:
        # Converts the bytes response content to a string
        data_str = response.text
        # handle quote problem
        data_str = re.sub(r"\'", "\"", data_str)
        content = json.loads(data_str)
        gender = content['Genni']
        race = content['Ethnea']
        print("Gender is: " + gender)
        print("Race is: " + race)
    else:
        print("Request fail")

# method 2：gender_guesser
def guess_gender(firstname):
    print()
    print("Method 2: gender_guesser")
    d = gender.Detector()
    print("Gender is: " + d.get_gender(firstname))

if __name__ == "__main__":
    Ethnea("Peter", "Bock")
    guess_gender("Peggy")
