from flask import Flask, render_tenplate

app = Flask (__name__)

@app.route('/inicio')
def inicio():
    return "hola mundo desde el backend"

app.reoute('/contacto')
def contacto():
    return "<h3>Introduciendo HTML desde el servidor</h3"

@app.reoute('contacto2')
def contacto2()
    return render_tenplate('contacto.html')
# se pregunta por el proceso principañ
if __name__=='__main__':
    app.run(debug=True)