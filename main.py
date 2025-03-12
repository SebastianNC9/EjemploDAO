from modelo import Usuario
from usuario_dao_impl import UsuarioDAOImpl

# Crear una instancia del DAO
dao = UsuarioDAOImpl()

def mostrar_menu():
    print("\n📌 Menú de opciones:")
    print("1️⃣ Insertar un nuevo usuario")
    print("2️⃣ Listar todos los usuarios")
    print("3️⃣ Buscar un usuario por ID")
    print("4️⃣ Actualizar un usuario")
    print("5️⃣ Eliminar un usuario")
    print("6️⃣ Salir")

while True:
    mostrar_menu()
    opcion = input("\n👉 Ingresa el número de la opción: ")

    if opcion == "1":
        nombre = input("🔹 Nombre del usuario: ")
        email = input("🔹 Email del usuario: ")
        usuario = Usuario(None, nombre, email)
        dao.insertar(usuario)
        print("✅ Usuario insertado correctamente.")

    elif opcion == "2":
        usuarios = dao.obtener_todos()
        if usuarios:
            print("\n📌 Lista de usuarios en la base de datos:")
            for u in usuarios:
                print(f"ID: {u.id}, Nombre: {u.nombre}, Email: {u.email}")
        else:
            print("\n⚠️ No hay usuarios registrados.")

    elif opcion == "3":
        try:
            id_usuario = int(input("🔍 Ingresa el ID del usuario a buscar: "))
            usuario = dao.obtener_por_id(id_usuario)
            if usuario:
                print(f"\n✅ Usuario encontrado: {usuario.nombre} ({usuario.email})")
            else:
                print("\n❌ Usuario no encontrado.")
        except ValueError:
            print("\n⚠️ Ingresa un número válido.")

    elif opcion == "4":
        try:
            id_usuario = int(input("✏️ Ingresa el ID del usuario a actualizar: "))
            usuario = dao.obtener_por_id(id_usuario)
            if usuario:
                nuevo_nombre = input("🔹 Nuevo nombre: ")
                nuevo_email = input("🔹 Nuevo email: ")
                usuario.nombre = nuevo_nombre
                usuario.email = nuevo_email
                dao.actualizar(usuario)
                print("\n✅ Usuario actualizado correctamente.")
            else:
                print("\n❌ Usuario no encontrado.")
        except ValueError:
            print("\n⚠️ Ingresa un número válido.")

    elif opcion == "5":
        try:
            id_usuario = int(input("🗑️ Ingresa el ID del usuario a eliminar: "))
            usuario = dao.obtener_por_id(id_usuario)
            if usuario:
                dao.eliminar(id_usuario)
                print("\n✅ Usuario eliminado correctamente.")
            else:
                print("\n❌ Usuario no encontrado.")
        except ValueError:
            print("\n⚠️ Ingresa un número válido.")

    elif opcion == "6":
        print("\n👋 Saliendo del programa. ¡Hasta luego!")
        break

    else:
        print("\n⚠️ Opción no válida. Inténtalo de nuevo.")
