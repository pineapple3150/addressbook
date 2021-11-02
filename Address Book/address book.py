from flask import Flask, render_template,request
from tinydb import TinyDB, Query
server = Flask(__name__)

db = TinyDB("contactlist.db")
#list_contact=[] can use if using a list to add contacts to contact list, isn't permanent, resets after server is stopped

@server.route("/")
def home():
    return render_template("homepage.html", **locals())

@server.route("/home")
def hompage():
    return render_template("homepage.html", **locals())

@server.route("/add")
def add():
    return render_template("addcontact.html", **locals())

@server.route("/confirm", methods=["post"])
def confirm():
    contact={} #is a dictionary
    contact["first_name"]=request.form.get("first_name")
    contact["last_name"]=request.form.get("last_name")
    contact["phone"]=request.form.get("phone")
    contact["email"]=request.form.get("email")
    #list_contact.append(contact): use if using a list
    db.insert(contact)   #saves permanently in a database
    return render_template("confirm.html")

@server.route("/list")
def list():
    contact_list = db.all()
    #use globals if using a list instead of database
    return render_template("listcontact.html", **locals())

@server.route("/delete/<phone>")
def delete(phone):
    contact = Query()
    db.remove(contact.phone == str(phone))
    return render_template ("listcontact.html", **locals())


if __name__ == "__main__":
    server.run(debug=True)