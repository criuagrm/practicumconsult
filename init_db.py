import sqlite3

# Conexión a la base de datos
conn = sqlite3.connect('practicum.db')
c = conn.cursor()

# Crear la tabla de trabajos de Prácticum
c.execute('''
    CREATE TABLE IF NOT EXISTS practicum (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        year INTEGER,
        author TEXT,
        practicum_level TEXT,
        title TEXT,
        description TEXT
    )
''')

# Insertar datos simulados
c.executemany('''
    INSERT INTO practicum (year, author, practicum_level, title, description)
    VALUES (?, ?, ?, ?, ?)
''', [
    (2022, 'Juan Pérez', 'II', 'Análisis de Políticas Públicas en Santa Cruz', 'Un estudio sobre las políticas de seguridad ciudadana.'),
    (2023, 'María García', 'III', 'Evaluación del Sistema de Salud', 'Análisis de los recursos en hospitales públicos en Bolivia.'),
    (2021, 'Luis Martínez', 'II', 'Impacto de la Educación en Zonas Rurales', 'Estudio de acceso y calidad educativa en comunidades rurales.'),
    (2022, 'Ana López', 'IV', 'Cambio Climático y Agricultura', 'Investigación sobre el impacto climático en la producción agrícola.'),
    (2020, 'Carlos Jiménez', 'III', 'Desigualdad Económica en Bolivia', 'Un análisis sobre los factores de desigualdad económica en el país.')
])

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()

print("Base de datos creada con datos simulados.")

