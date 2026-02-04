🌦️ Web App OpenWeather - Streamlit
Este é um projeto desenvolvido para colocar em prática o consumo de APIs com autenticação, tratamento de dados JSON e deploy de aplicações web utilizando Python e Streamlit.

O aplicativo permite que o utilizador consulte em tempo real as condições meteorológicas de qualquer cidade do mundo, utilizando os dados oficiais da OpenWeatherMap.

🚀 Funcionalidades
    🔍 Busca por nome da cidade.
    🌡️ Exibição de Temperatura e Sensação Térmica.
    💧 Índice de Humidade e Cobertura de Nuvens.
    📱 Interface responsiva e intuitiva.

🛠️ Tecnologias Utilizadas
 - Linguagem: Python 3.12
 - Framework Web: Streamlit
 - Consumo de API: Requests
 - Gestão de Variáveis de Ambiente: python-dotenv
 - Deploy: Streamlit Cloud

🔒 Segurança e Boas Práticas
Para este projeto, foram aplicadas técnicas de segurança para proteção da API Key:
 - Utilização de ficheiro .env para desenvolvimento local.
 - Configuração de Secrets Management no Streamlit Cloud para produção.
 - Configuração de .gitignore para impedir o upload de credenciais sensíveis para o GitHub.

📥 Como executar o projeto localmente
1. Clone o repositório:
git clone https://github.com/nayarasudariodiniz/web_app_api_weather_streamlit.git

2. Instale as dependências:
pip install -r requirements.txt

3. Crie um ficheiro .env na raiz do projeto e adicione sua chave:
CHAVE_API_OPENWEATHER=sua_chave_aqui

4. Execute o app:
streamlit run web_app_open_weather.py

💡 Desenvolvido por Nayara Diniz
