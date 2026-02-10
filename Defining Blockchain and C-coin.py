
#importing all libraries. (You can get an idea of what to work on by looking at the libraries.)
import datetime
import hashlib
import json
from flask import Flask, jsonify, request
import requests
from uuid import uuid4
from urllib.parse import urlparse


#Building the blockchain

class Blockchain:
    def __init__(self): # initializing the blockchain
        self.chain= []
        self.transactions=[]
        self.create_block(proof = 1, previous_hash= '0')
        self.nodes= set()
        
    def create_block(self, proof, previous_hash): # definition of blockchain
        block = {'index': len(self.chain)+1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash,
                 'transactions': self.transactions}
        self.transactions=[]        
        self.chain.append(block)
        return block
    
    def get_previous_block(self):
        return self.chain[-1]
    
    
    def proof_of_work(self, previous_proof):
        pass
        #create a proof of work for the block
        # WRITE YOUR CODE HERE AND REMOVE "pass"
        ###################################

        ###################################
    
    def hash(self, block): # hashing the block
        encoded_block= json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    
    def is_chain_valid(self, chain):
        pass
        #Create a function to check if the chain is valid
        # WRITE YOUR CODE HERE AND REMOVE "pass"
        ###################################
        
        ###################################
    
    def add_transaction(self, sender, receiver, amount):
        pass
        # Create a function to add a transaction to the blockchain
        # WRITE YOUR CODE HERE AND REMOVE "pass"
        ###################################
        
        ###################################
    
    def add_node(self, address):
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)
   # Updated replace_chain Function
 
    def replace_chain(self):
        network = self.nodes
        longest_chain = None
        max_length = len(self.chain)

        for node in network:
           response = requests.get(f'http://{node}/get_chain')
           if response.status_code == 200:
               length = response.json()['length']
               chain = response.json()['chain']
               if length > max_length and self.is_chain_valid(chain):
                   max_length = length
                   longest_chain = chain

        if longest_chain:
           self.chain = longest_chain
           return True
    
        return False

#Mining the blockchain

#Creating the Web App

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR']= False

#Creating an address for the node on Port 5000
node_address= str(uuid4()).replace('-', '')

#Creating the blockchain instance

blockchain = Blockchain()




#Mining a new block

@app.route('/mine_block', methods= ['GET'])
def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)

    block = blockchain.create_block(proof, previous_hash)

    response = {
        'message': 'Congratulations, you just mined a block!',
        'index': block['index'],
        'timestamp': block['timestamp'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash']
    }
    return jsonify(response), 200



#Get the full blockchain

@app.route('/get_chain', methods=['GET'])
def get_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    return jsonify(response), 200

    

#Checking if blockchain is valid

@app.route('/is_valid', methods= ['GET'])
def is_valid():
    pass 
    #Create a route to check if the blockchain is valid
    # WRITE YOUR CODE HERE AND REMOVE "pass"
    ###################################
        
    ###################################


#Adding a new transaction to the blockchain
@app.route('/add_transaction', methods= ['POST'])
def add_transaction():
    pass
    #Create a route to add a transaction to the blockchain
    # WRITE YOUR CODE HERE AND REMOVE "pass"
    ###################################
        
    ###################################


#Decentralizing the blockchain

#connecting new nodes
@app.route('/connect_node', methods= ['POST'])
def connect_node():
    pass
    #Create a route to connect a new node
    # WRITE YOUR CODE HERE AND REMOVE "pass"
    ###################################
        
    ###################################





#Running the App
app.run(host='0.0.0.0', port=5000, debug=True)
