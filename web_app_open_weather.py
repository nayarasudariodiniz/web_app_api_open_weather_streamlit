from pprint import pprint
import requests
import dotenv
import os
import streamlit as st

def fazer_requests(url, params=None):
    resposta = requests.get(url, params=params)
    try:
        resposta.raise_for_status()
    except requests.HTTPError as e:
        print(f'Erro no request: {e}')
        resultado = None
    else:
        resultado = resposta.json()
        return resultado

def pegar_tempo_para_local(local):
    dotenv.load_dotenv()
    token = os.getenv('CHAVE_API_OPENWEATHER') or st.secrets.get('CHAVE_API_OPENWEATHER')
    if not token:
        st.error("Erro: Chave da API não encontrada!")
        st.stop()
        
    url = f'https://api.openweathermap.org/data/2.5/weather'
    # headers = {
    #    'Authorization': f'Bearer {token}'
    # }
    params = {
        'appid': token,
        'q': local,
        'units': 'metric',
        'lang': "pt_br",
        }
    resposta = requests.get(url=url,
    #                        headers=headers,
                            params=params)
    dados_tempo = fazer_requests(url=url, params=params)
    return dados_tempo

def main():
    st.title('Web App - Open Weather (Previsão do tempo)')
    st.write('Dados do OpenWeather (https://openweathermap.org/current)')
    local = st.text_input('Busque uma cidade:')
    if not local:
        st.stop()
    
    dados_tempo = pegar_tempo_para_local(local=local)
    if not dados_tempo:
        st.warning(f"Dados não encontrados para a cidade {local}")
        st.stop()
    clima_atual = dados_tempo['weather'][0]['description']
    temperatura = dados_tempo['main']['temp']
    sensacao_termica = dados_tempo['main']['feels_like']
    umidade = dados_tempo['main']['humidity']
    cobertura_nuvens = dados_tempo['clouds']['all']

    st.metric(label='Condição', value = clima_atual)
       
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label='Temperatura', value = f'{temperatura} °C')
        st.metric(label='Sensação Térmica', value=f'{sensacao_termica} °C')
    with col2:
        st.metric(label = 'Umidade', value = f'{umidade} % ')
        st.metric(label ='Cobertura de nuvens', value = f'{cobertura_nuvens} °C ')


if __name__ == '__main__':

    main()
