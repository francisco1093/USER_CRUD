import requests


TEST_USER = {
    "first_name":"John",
    "last_name":"Doe",
    "hobbies":"Skiing",
    "active":1
}

def test_user_creation():
    out = requests.post("http://127.0.0.1:5000/users",json=TEST_USER)
    if out.status_code==201:
        print(out.json())
    else:
        print("Something went wrong")

def test_user_get():
    out = requests.get("http://127.0.0.1:5000/users/1")
    print(out.status_code)
    if out.status_code==200:
        print(out.json())
    else:
        print("Something went wrong")


def test_user_deactivate():
    out = requests.delete("http://127.0.0.1:5000/users/2")
    if out.status_code ==200:
        print(out.json())
    else:
        print("Something is wrong with delete")

def test_user_delete():
    out = requests.delete("http://127.0.0.1:5000/users/delete/1")
    if out.status_code ==200:
        print(out.json())
    else:
        print("Something is wrong with delete")

def test_user_update(attr, new_value):
    out = requests.put("http://127.0.0.1:5000/users/1/"+attr+"/"+new_value)
    if out.status_code ==200:
        print(out.json())
    else:
        print("Something is wrong with update")

if __name__=="__main__":
    test_user_creation()
    #test_user_update("first_name","new_name_TEST")
    #test_user_deactivate()
    #test_user_get()
    #test_user_delete()