from flask import Flask, request , render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Ejercicio1.html', methods=['GET','POST'])
def Ejercicio1():
    if request.method == 'POST':
        nombre = str(request.form['nombre'])
        edad = int(request.form['edad'])
        tarros = int(request.form['tarros'])
        precio = tarros*9000
        if edad >= 18 and edad <= 30:
            descuento = precio*0.15
            preciofinal = precio-descuento
        if edad > 30:
            descuento = precio * 0.25
            preciofinal = precio - descuento
        else:
            descuento = 0
            preciofinal = precio
        return render_template('Ejercicio1.html', nombre=nombre, precio=precio,descuento=descuento, preciofinal=preciofinal)
    return render_template('Ejercicio1.html')
@app.route('/Ejercicio2.html', methods=['GET', 'POST'])
def Ejercicio2():
    if request.method == 'POST':
        usuario = str(request.form['usuario'])
        contraseña = str(request.form['contraseña'])
        if usuario == "juan" and contraseña == "admin":
            frase = "Bienvenido Administrador juan"
        elif usuario == "pepe" and contraseña == "user":
            frase = "Bienvenido Usuario pepe"
        else:
            frase = "Usuario o contraseña incorrectos"
        return render_template('Ejercicio2.html', frase=frase)
    return render_template('Ejercicio2.html')
if __name__ == '__main__':
    app.run(debug=True)