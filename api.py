from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import json
import ast
import tictactoe as ttt
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)
EMPTY = None
parser = reqparse.RequestParser()
parser.add_argument('board', action='append')
def boarddecoder(board):
        l=[]
        for i in range(3):
            list = ast.literal_eval(board[i])
            l.append(list)

        return l
def actiondecoder(act):
        l=[]
        for i in range(2):
            list = ast.literal_eval(act[i])
            l.append(list)

        return l

class initialboard(Resource):
    @cross_origin()
    def get(self):
        board=[[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
        return board
    @cross_origin()
    def post(self):
        parser.add_argument('action', action='append')
        args =  parser.parse_args()
        board= boarddecoder(args['board']) 
        action= actiondecoder(args['action'])
        result= ttt.result(board, action)  
        return json.dumps(result)
class player(Resource):
    @cross_origin()
    def post(self):
        args =  parser.parse_args()
        board= boarddecoder(args['board']) 
        result= ttt.player(board)
        return json.dumps(result)
class winner(Resource):
    @cross_origin()
    def post(self):
        args =  parser.parse_args()
        board= boarddecoder(args['board']) 
        result= ttt.terminal(board)
        return json.dumps(result)
class minimax(Resource):
    @cross_origin()
    def post(self):
        args =  parser.parse_args()
        board= boarddecoder(args['board']) 
        result= ttt.minimax(board)
        
        return json.dumps(result)
api.add_resource(initialboard, '/board')
api.add_resource(winner, '/winner')
api.add_resource(minimax, '/minimax')
api.add_resource(player, '/player')

if __name__ == '__main__':
    app.run(debug=True)