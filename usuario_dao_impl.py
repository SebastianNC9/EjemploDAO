import sqlite3
from modelo import Usuario
from usuario_dao import UsuarioDAO

class UsuarioDAOImpl(UsuarioDAO):
    def __init__(self, db_path="usuarios.db"):
        self.db_path = db_path
        self._crear_tabla()

    def _crear_tabla(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE
                )
            ''')
            conn.commit()

    def insertar(self, usuario):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO usuarios (nombre, email) VALUES (?, ?)",
                           (usuario.nombre, usuario.email))
            conn.commit()

    def obtener_por_id(self, id):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE id = ?", (id,))
            row = cursor.fetchone()
            return Usuario(*row) if row else None

    def obtener_todos(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuarios")
            return [Usuario(*row) for row in cursor.fetchall()]

    def actualizar(self, usuario):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE usuarios SET nombre = ?, email = ? WHERE id = ?",
                           (usuario.nombre, usuario.email, usuario.id))
            conn.commit()

    def eliminar(self, id):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))
            conn.commit()
