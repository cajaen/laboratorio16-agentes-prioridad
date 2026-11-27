import unittest

from tareas import agregar, pendientes


class PruebasTareasIniciales(unittest.TestCase):
    def test_crear_primera_tarea(self):
        registros = []
        self.assertEqual(agregar(registros, "Revisar agenda")["id"], 1)

    def test_rechazar_titulo_sin_contenido(self):
        with self.assertRaises(ValueError):
            agregar([], "   ")


if __name__ == "__main__":
    unittest.main()
