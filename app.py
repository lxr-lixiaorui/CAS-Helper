# app.py
from flask import Flask, render_template, request, jsonify
import funcs
app = Flask(__name__)



def funcc(prom):
    processed = ''.join([c if i%2==0 else c.upper() for i, c in enumerate(prom)])
    return f"模式C处理结果：{processed}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    prom = data['prompt']
    mode = data['mode']
    
    if mode == 'A':
        result = funcs.casRecord(prom)
    elif mode == 'B':
        result = funcs.clubReflection(prom)
    elif mode == 'C':
        result = funcc(prom)
    else:
        result = "Error: Invaild Operation"
    
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=1145)