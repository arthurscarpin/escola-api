# 📚 API Escola

Essa API RESTful de uma escola foi desenvolvida para colocar em prática os conhecimentos adquiridos em Django Rest Framework. 

## 🚀 Tecnologias utilizadas
<div align="left">
    <a href="https://skillicons.dev">
        <img src="https://skillicons.dev/icons?i=python,django,sqlite"/>
    </a>
</div>

## 🎒 API RESTful
- Interface Django Rest Framework:

![interface-django-api](https://github.com/user-attachments/assets/c4583393-8f81-48de-a797-d5066d84c0e7)

- Interface Django Admin:

![interface-django-admin](https://github.com/user-attachments/assets/4fa871a2-3f85-4be2-9d92-af24412569f5)

## 🖥️ Documentação

Essa API foi documentada através do **Swagger** e **Redoc**.

- Documentação Swagger:

![api-escola-swagger](https://github.com/user-attachments/assets/ffac2a2a-843d-40b5-a5a1-3a850ad266dc)

```
# Url:
<localhost>/swagger
```

- Documentação Redoc:

![api-escola-redoc](https://github.com/user-attachments/assets/f10282f3-01d4-4b58-9ab6-36c010b67361)

```
# Url:
<localhost>/redoc
```

## 🛠️ Como executar?
Para executar esse projeto é necessário seguir o passo a passo a seguir:

1. Criar o ambiente virtual do Python.

Na pasta raíz do repositório local, execute o comando:
```
python -m venv <nome do ambiente virtual>
```

2. Ativar o ambiente virutal
```
.\venv\Scripts\activate
```

3. Instalar as dependências do **requirements.txt**.
```
pip install -r requirements.txt
```

4. Executar as Migrations para preparar o banco de dados.
```
python manage.py migrate
```

5. Executar os comandos a seguir para popular as tabelas do banco de dados utilizando dados **Fake** para testes.
```
# Popular tabela de cursos:
python popular_banco_cursos.py

# Popular tabela de estudantes:
python popular_banco_estudantes.py
```

6. Executar o comando a seguir para ativar o servidor da aplicação Django:
```
python .\manage.py runserver
```

## 📝 Testes
Para testar essa API, você poderá utilizar o **Postman**:

Esse link contém um totorial de como usar a ferramenta: [Tutorial Postman](https://gist.github.com/zec4o/f4a600fafa50003e315fa3fcfd9c1e4a)

## 📁 Documentações de referência
[Documentação Django](https://www.djangoproject.com/)
<br>
[Documentação Django Rest Framework](https://www.django-rest-framework.org/)
