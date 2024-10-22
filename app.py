from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'  # Cambia esto por una clave secreta más fuerte

# Datos de ejemplo de usuarios (en un entorno real, esto vendría de una base de datos)
usuarios = {
    'Erland': '123456789',
    'Erland Chambi': '1324'
}

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username in usuarios and usuarios[username] == password:
            session['username'] = username
            return redirect(url_for('welcome'))
        else:
            flash('Nombre de usuario o contraseña incorrectos.')
    
    return render_template('login.html')

@app.route('/welcome')
def welcome():
    if 'username' in session:
        username = session['username']
        return render_template('welcome.html', username=username)
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
