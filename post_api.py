from flask import Flask,jsonify,request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

def Data_kontrol(PostedData, functionName):
    if (functionName == "topla" or functionName == "cikar" or functionName == "carp"):
        if "x" not in PostedData or "y" not in PostedData:
            return 301
        else:
            return 200
    elif (functionName == "bolme"):
        if "x" not in PostedData or "y" not in PostedData:
            return 301
        elif int(PostedData["y"]) == 0:
            return 302
        else:
            return 200



class Topla(Resource):
    def post(self):

        PostedData = request.get_json()

        status_code = Data_kontrol(PostedData, "topla")
        if (status_code!=200):
            retJson = {
                "Message" : "HATA!!! x ve y degerini giriniz !!!",
                "Status Code" : status_code
            }
            return jsonify(retJson)

        x = PostedData["x"]
        y = PostedData["y"]
        x = int(x)
        y = int(y)
        ret = x+y
        retMap = {
            'Message' : ret,
            'Status Code' : 200
        }
        return jsonify(retMap)

class Cikar(Resource):
    def post(self):
        PostedData = request.get_json()

        status_code = Data_kontrol(PostedData, "cikar")
        if (status_code != 200):
            retJson = {
                "Message": "HATA!!! x ve y degerini giriniz !!!",
                "Status Code": status_code
            }
            return jsonify(retJson)

        x = PostedData["x"]
        y = PostedData["y"]
        x = int(x)
        y = int(y)
        ret = x - y
        retMap = {
            'Message': ret,
            'Status Code': 200
        }
        return jsonify(retMap)

class Carp(Resource):
    def post(self):
        PostedData = request.get_json()

        status_code = Data_kontrol(PostedData, "carp")
        if (status_code != 200):
            retJson = {
                "Message": "HATA!!! x ve y degerini giriniz !!!",
                "Status Code": status_code
            }
            return jsonify(retJson)

        x = PostedData["x"]
        y = PostedData["y"]
        x = int(x)
        y = int(y)
        ret = x * y
        retMap = {
            'Message': ret,
            'Status Code': 200
        }
        return jsonify(retMap)

class Bolme(Resource):
    def post(self):
        PostedData = request.get_json()

        status_code = Data_kontrol(PostedData, "bolme")
        if (status_code != 200):
            retJson = {
                "Message": "HATA!!! x ve y degerini giriniz !!!",
                "Status Code": status_code
            }
            return jsonify(retJson)

        x = PostedData["x"]
        y = PostedData["y"]
        x = int(x)
        y = int(y)
        ret = (x*1.0)/ y
        retMap = {
            'Message': ret,
            'Status Code': 200
        }
        return jsonify(retMap)

api.add_resource(Topla, "/topla")
api.add_resource(Cikar, "/cikar")
api.add_resource(Carp, "/carp")
api.add_resource(Bolme, "/bolme")

@app.route('/')
def hello_world():
    return "Hello world"


if __name__ == "__main__":
    app.run(debug=True)
