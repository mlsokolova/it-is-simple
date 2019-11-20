#
# Simple Flask app
#
from flask import Flask
from flask import request, abort, make_response, jsonify
import cx_Oracle
import requests
import os
import json


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, world!"

@app.route("/get_table_content", methods=["GET"])
def get_table_content():
    def jsonify_result(data, headers):
        dict = {}
        for i in range(len(headers)):
            dict[headers[i][0]]=data[i]
        return dict

    conn = cx_Oracle.connect("hr","hr","XE")
    cur = conn.cursor()
    schema=request.args.get("schema", default = "", type = str)
    table=request.args.get("table", default = 'dual', type = str)
    if schema == "": query = "select * from {}".format(table)
    else: query = "select * from {}.{}".format(schema,table)
    cur.execute(query)
    query_result = cur.fetchall()
    result=json.dumps(list(map(lambda x: jsonify_result(x,cur.description), query_result)))
    return result

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Not found. Bad luck!"}), 404)

if __name__ == "__main__":
    os.environ["ORACLE_HOME"]="/home/masha/Downloads/instantclient_19_3"
    os.environ["LD_LIBRARY_PATH"]="/home/masha/Downloads/instantclient_19_3"
    app.run(debug=True, host="0.0.0.0")



