# 🌦️ Web App OpenWeather - Streamlit

Este é um projeto desenvolvido para colocar em prática o consumo de **APIs com autenticação**, tratamento de dados JSON e deploy de aplicações web utilizando **Python** e **Streamlit**.

O aplicativo permite que o utilizador consulte em tempo real as condições meteorológicas de qualquer cidade do mundo, utilizando os dados oficiais da [OpenWeatherMap](https://openweathermap.org/).

## 🚀 Funcionalidades
* 🔍 **Busca por nome da cidade:** Encontre dados climáticos de qualquer lugar.
* 🌡️ **Exibição de Temperatura:** Veja a temperatura atual e a sensação térmica.
* 💧 **Indicadores de Umidade:** Acompanhe a umidade relativa e a cobertura de nuvens.
* 📱 **Interface Intuitiva:** UI desenvolvida para ser clara e responsiva.

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3.12
* **Framework Web:** [Streamlit](https://streamlit.io/)
* **Consumo de API:** Requests
* **Gestão de Variáveis de Ambiente:** `python-dotenv`
* **Deploy:** Streamlit Cloud

## 🔒 Segurança e Boas Práticas
Para este projeto, foram aplicadas técnicas de segurança para proteção da **API Key**:
* Utilização de ficheiro `.env` para desenvolvimento local.
* Configuração de **Secrets Management** no Streamlit Cloud para produção.
* Configuração de `.gitignore` para impedir o upload de credenciais sensíveis para o GitHub.

## 📥 Como executar o projeto localmente

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/nayarasudariodiniz/web_app_api_weather_streamlit.git](https://github.com/nayarasudariodiniz/web_app_api_weather_streamlit.git)

2. **Instale as dependências:**
   ```bash
    pip install -r requirements.txt

4. **Crie um ficheiro .env na raiz do projeto e adicione sua chave:**
    ```bash
    CHAVE_API_OPENWEATHER=sua_chave_aqui

5. **Execute o app:**
   ```bash
   streamlit run web_app_open_weather.py

💡 Desenvolvido por Nayara Diniz
