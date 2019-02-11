from flask import Flask, render_template

app = Flask(__name__) # Para poder crear las rutas del servidor

@app.route('/')
def home():
    return render_template('home.html') # Renderizar un html dependiendo de la URL

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/products')
def products():
    return render_template('products.html')

if __name__ == '__main__':
    app.run(debug=True)