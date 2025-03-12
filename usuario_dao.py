from abc import ABC, abstractmethod

class UsuarioDAO(ABC):
    @abstractmethod
    def insertar(self, usuario):
        pass

    @abstractmethod
    def obtener_por_id(self, id):
        pass

    @abstractmethod
    def obtener_todos(self):
        pass

    @abstractmethod
    def actualizar(self, usuario):
        pass

    @abstractmethod
    def eliminar(self, id):
        pass
