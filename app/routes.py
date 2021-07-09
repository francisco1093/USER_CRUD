from flask import Flask, request

from app.database import (
     read_user,
     scan, 
     insert,
    deactivate_user,
    update_user,
    delete_user_table
)

app = Flask(__name__)

@app.route("/users")
def get_all_users():
    out = {"ok":True,
            "message":"Success"
            }
    out["body"]=scan()
    return out

@app.route("/users/<int:uid>",methods=["GET"])
def get_user(uid):
    out = {"ok":True,
            "message":"Success"
            }
    out["body"]=read_user(uid)
    return out,200

@app.route("/users",methods=["POST"])
def create_user():
    out = {
        "ok":True,
        "message":"Sucess"
    }

    user_data = request.json
    out["last_row_id"] = insert(
        
        user_data.get("first_name"),
        user_data.get("last_name"),
        user_data.get("hobbies"),
        user_data.get("active"),
        
    )
    return out, 201

@app.route("/users/<int:uid>", methods=["DELETE"])
def delete_user(uid):
    out = {
        "ok":True,
        "message":"Success"
    }
    deactivate_user(uid)
    return out, 200

@app.route("/users/delete/<int:uid>", methods=["DELETE"])
def delete_user_permanent(uid):
    out = {
        "ok":True,
        "message":"Success"
    }
    delete_user_table(uid)
    return out, 200

@app.route("/users/<int:uid>/<string:attri>/<string:value>", methods=["PUT"])
def update_user_value(uid,attri,value):
    attr=attri
    new_value="JESUsSd"
    out = {
        "ok":True,
        "message":"Success"
    }
    update_user(uid,attri,value)
    return out, 200


@app.route("/agent")
def agent():
    user_agent = request.headers.get("User-Agent")
    return "<p> Your user agent is: %s" % user_agent