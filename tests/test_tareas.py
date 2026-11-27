import unittest

from tareas import agregar, filtrar_por_prioridad, pendientes


class PruebasTareasIniciales(unittest.TestCase):
    def test_crear_primera_tarea(self):
        registros = []
        self.assertEqual(agregar(registros, "Revisar agenda")["id"], 1)

    def test_compatibilidad_asigna_media(self):
        registro = agregar([], "Preparar reporte")
        self.assertEqual(registro["prioridad"], "media")

    def test_admite_cada_prioridad(self):
        for nivel in ("alta", "media", "baja"):
            with self.subTest(nivel=nivel):
                self.assertEqual(agregar([], "Caso", nivel)["prioridad"], nivel)

    def test_nivel_fuera_del_catalogo(self):
        with self.assertRaises(ValueError):
            agregar([], "Caso", "inmediata")

    def test_seleccionar_prioridad(self):
        registros = []
        agregar(registros, "Restablecer servicio", "alta")
        agregar(registros, "Actualizar guía", "baja")
        agregar(registros, "Comprobar respaldo", "alta")
        resultado = filtrar_por_prioridad(registros, "alta")
        self.assertEqual([x["id"] for x in resultado], [1, 3])

    def test_filtro_valida_el_nivel(self):
        with self.assertRaises(ValueError):
            filtrar_por_prioridad([], "urgente")

    def test_pendientes_no_expone_la_lista_original(self):
        registros = []
        agregar(registros, "Revisar agenda")
        vista = pendientes(registros)
        self.assertEqual(vista, registros)
        self.assertIsNot(vista, registros)

    def test_rechazar_titulo_sin_contenido(self):
        with self.assertRaises(ValueError):
            agregar([], "   ")


if __name__ == "__main__":
    unittest.main()
