from django.test import TestCase
from escola.models import Estudante, Curso

class FixturesTestCase(TestCase):
    fixtures = ['prototipo_banco.json']

    def test_carregamento_da_fixtures(self):
        '''Teste que verifica o carregamento da fixtures'''
        estudante = Estudante.objects.get(cpf='88249482514')
        curso = Curso.objects.get(pk=3)
        self.assertEqual(estudante.celular, '11 94730-9193')
        self.assertEqual(curso.codigo, 'CPOO1')
