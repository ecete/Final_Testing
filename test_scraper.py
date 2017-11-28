import unittest
from orm import *
from Usuario import *
from StackEntryFeed import StackEntryFeed
from prueba_orm import SetAll
from unittest.mock import Mock, patch

class TestWebScraper(unittest.TestCase):
    
    def setUp(self):
        self.orm = OrmFactory()
        self.mock_pregunta = Mock(question = "pregunta random",explicacion = "porque se necesita",linkpregunta = "link random")
        self.mock_respuesta = Mock(idpregunta = 24, respuesta = "respuesta cualquiera", fecha = "11/11/11", linkrespuesta = "link bueno")
        self.mock_usuario = Mock(username = "Estanislao", userid = 66394,biografia = "Prefiere no...", comunidades = "StackOverflow", linkusuario = "estanislao.com", url = "https://es.stackoverflow.com/questions/120861/buscar-seguidores-de-una-cuenta-de-twitter-usando-python")
        self.u = Usuario(self.mock_usuario.url,self.mock_usuario.username,self.mock_usuario.userid)

    def test_username(self):        
        self.assertEqual(self.u.get_username(), "Estanislao")
    
    def test_id(self):
        self.assertEqual(self.u.get_userid(),66394)
    
    def test_communities(self):
        self.assertEqual(self.u.get_comunidades(), [])
    
    @patch('StackEntryFeed.StackEntryFeed.get_fecha_publicacion')
    def test_date(self, MockFecha):
        fecha = MockFecha()
        fecha.get_fecha_publicacion.return_value = [
        {
        'fecha': '08/01/2017'
        }
        ]
        response = fecha.get_fecha_publicacion()
        self.assertIsNotNone(response)
        self.assertIsInstance(response[0], dict)
    
    def test_add_user(self):
        self.assertIsNone(self.orm.agregaUsuario(self.mock_usuario.username,self.mock_usuario.biografia,self.mock_usuario.comunidades,self.mock_usuario.userid,self.mock_usuario.linkusuario))
    
    def test_add_answer(self):
        self.assertIsNone(self.orm.agregaRespuesta(self.mock_respuesta.idpregunta,self.mock_respuesta.respuesta,self.mock_respuesta.fecha,self.mock_usuario.userid, self.mock_respuesta.linkrespuesta))
    
    def test_add_question(self):
        self.assertIsNone(self.orm.agregaPregunta(self.mock_respuesta.idpregunta,self.mock_pregunta.question,self.mock_pregunta.explicacion,self.mock_usuario.userid,self.mock_pregunta.linkpregunta))

if __name__ == '__main__':
    unittest.main()