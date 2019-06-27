from app import app
@app.route('/index')
def index():
    a=5
    b=4
    return str(a-b)
@app.route('/udit')
def udit():
    return('udit arora')
@app.route('/vaibhav')
def vaibhav():
    return('/vaibhav sharma')
@app.route('/vikalp')
def vikalp():
    return ('/ vikalp kaushik')

        
    

