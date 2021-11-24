from flask import Flask, request
from flask_restful import Resource, Api, abort, reqparse
from filldb import PatentePipeline 

app = Flask(__name__)
api = Api(app)

def createDb():
    pipeline = PatentePipeline()
    pipeline.open_session()
    print(pipeline.fulldb())
    pipeline.close_session()

class GetPosition(Resource):
    def get(self,patent):
        pipeline = PatentePipeline()
        pipeline.open_session()
        id = pipeline.get_id(patent)
        pipeline.close_session()
        return id

class GetPatent(Resource):
    def get(self,id):
        pipeline = PatentePipeline()
        pipeline.open_session()
        patente = pipeline.get_patent(int(id))
        pipeline.close_session()
        return patente

api.add_resource(GetPosition, "/position/<string:patent>")
api.add_resource(GetPatent, "/patent/<int:id>")

if __name__ == "__main__":
    createDb()
    app.run(debug=True)