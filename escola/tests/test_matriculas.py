from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Estudante, Curso, Matricula
from escola.serializers import MatriculaSerializer

class MatriculasTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin', password='admin')
        self.url = reverse('Matriculas-list')
        self.client.force_authenticate(user=self.usuario)
        self.estudante_01 = Estudante.objects.create(
            nome='Teste estudante um',
            email='testeestudante01@email.com',
            cpf='40093565020',
            data_nascimento='2024-01-01',
            celular='86 99999-9999'
        )
        self.curso_01 = Curso.objects.create(
            codigo='POO',
            descricao='Curso de python orientado a objetos',
            nivel='B'
        )
        self.matricula_01 = Matricula.objects.create(
            estudante=self.estudante_01,
            curso=self.curso_01,
            periodo='M'
        )

    def test_requisicao_get_para_listar_matriculas(self):
        '''Teste de requisição GET'''
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_get_para_listar_um_curso(self):
        '''Teste de requisição GET para uma matricula'''
        response = self.client.get(self.url + '1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dados_matricula = Matricula.objects.get(pk=1)
        dados_matricula_serializados = MatriculaSerializer(instance=dados_matricula).data
        self.assertEqual(response.data, dados_matricula_serializados)

    def test_requisicao_post_para_criar_uma_matricula(self):
        '''Teste de requisição POST para um curso'''
        dados = {
            'estudante': self.estudante_01.pk,
            'curso': self.curso_01.pk,
            'periodo': 'M'
        }
        response = self.client.post(self.url, dados)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_delete_uma_matricula(self):
        '''Teste de requisição DELETE um curso'''
        response = self.client.delete(self.url + '2/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_requisicao_put_para_atualizar_uma_matricula(self):
        '''Teste de requisição PUT para um matricula'''
        dados = {
            'estudante': self.estudante_01.pk,
            'curso': self.curso_01.pk,
            'periodo': 'M'
        }
        response = self.client.put(self.url + '1/', dados)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)