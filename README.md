#Eventex

Sistema de Eventos encomendado pela Morena

##Como desenvolver
1. Clone o repositório
2. crie um virtualenv com o Python 3.9.6
3. Ative o virtualenv
4. Instale as dependências
5. Configure a instancia com o .env
6. Execute os testes

```console
git clone git@github.com/brunomak77/wttd.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```

##Como fazer deploy
1. Crie uma instância no Heroku
2. Envie as configurações para o Heroku
3. Defina uma SECRET_KEY segura para a instância
4. Defina DEBUG=False
5. Configure o serviço de email
6. Envie o código para o Heroku

```console
heroku create minhainstacia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
#configuro o email
git push heroku master --force
```