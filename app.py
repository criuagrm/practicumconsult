from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Cambia esta clave para seguridad

# Conexión a la base de datos
def get_db_connection():
    conn = sqlite3.connect('practicum.db')
    conn.row_factory = sqlite3.Row
    return conn

# Página de inicio
@app.route('/')
def index():
    return render_template('index.html')

# Página de búsqueda de trabajos
@app.route('/search', methods=['GET', 'POST'])
def search():
    conn = get_db_connection()
    if request.method == 'POST':
        # Obtener los datos del formulario
        year = request.form['year']
        author = request.form['author']
        practicum_level = request.form['practicum_level']
        keyword = request.form['keyword']

        # Consulta dinámica en base a filtros
        query = "SELECT * FROM practicum WHERE 1=1"
        params = []
        if year:
            query += " AND year = ?"
            params.append(year)
        if author:
            query += " AND author LIKE ?"
            params.append(f'%{author}%')
        if practicum_level:
            query += " AND practicum_level = ?"
            params.append(practicum_level)
        if keyword:
            query += " AND title LIKE ?"
            params.append(f'%{keyword}%')
        
        results = conn.execute(query, params).fetchall()
        conn.close()
        return render_template('search.html', results=results)
    
    return render_template('search.html', results=[])

# Detalle de un trabajo específico
@app.route('/detail/<int:id>')
def detail(id):
    conn = get_db_connection()
    work = conn.execute('SELECT * FROM practicum WHERE id = ?', (id,)).fetchone()
    conn.close()
    return render_template('detail.html', work=work)

# Formulario para solicitar el trabajo
@app.route('/request/<int:id>', methods=['POST'])
def request_work(id):
    # Simulación de una solicitud; aquí puedes añadir lógica para enviar un correo u otra acción.
    flash('Solicitud enviada con éxito. Puedes recoger el trabajo en la oficina.')
    return redirect(url_for('detail', id=id))

if __name__ == '__main__':
    app.run(debug=True)

