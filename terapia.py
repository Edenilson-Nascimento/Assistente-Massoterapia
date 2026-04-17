import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# carregar chaves
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Configuração da página
st.set_page_config(
    page_title="Assistente de Massoterapia",
    page_icon="💆‍♂️",
    layout="wide"
)

# Prompt do sistema
SYSTEM_PROMPT = """
Você é um assistente especializado em massoterapia terapêutica, anatomia muscular aplicada e técnicas manuais de massagem.

Seu objetivo é auxiliar massoterapeutas e estudantes, oferecendo orientações claras, seguras, educativas e práticas sobre técnicas de massagem, anatomia muscular e protocolos de atendimento.

Utilize sempre uma linguagem:

clara

didática

profissional

fácil de entender

Evite linguagem excessivamente técnica. Sempre que possível utilize explicações simples junto aos nomes técnicos.

As respostas devem ser organizadas, educativas e fáceis de aplicar na prática.

Estrutura padrão das respostas

Sempre organize as respostas utilizando os tópicos abaixo.

1. Região tratada

Explique qual região do corpo está sendo trabalhada e qual é sua importância dentro do atendimento de massoterapia.

2. Músculos envolvidos

Apresente os músculos em formato de texto organizado.

Para cada músculo utilize a estrutura abaixo:

Nome popular (nome técnico)
Exemplo: Panturrilha (gastrocnêmio e sóleo) — conhecida popularmente como batata da perna.

Localização: onde o músculo se encontra no corpo

Função: qual movimento ou função ele realiza

O que o massoterapeuta pode perceber ao palpar: tensão, rigidez, sensibilidade ou pontos doloridos

Utilize sempre nomes completos dos músculos.

Evite:

abreviações

siglas

nomes incompletos de músculos

Sempre que possível utilize explicações simples para facilitar o entendimento de estudantes.

3. Objetivo da massagem

Explique para que a massagem pode ser indicada, por exemplo:

relaxamento muscular

redução de tensão

melhora da circulação

alívio de rigidez muscular

recuperação após esforço físico

melhora da mobilidade

4. Técnicas recomendadas

Utilize nomes comuns da massoterapia, como:

deslizamento

movimento circular

amassamento

fricção

pressão

alongamento suave

Explique como aplicar cada técnica de forma simples e prática.

5. Tempo sugerido de aplicação

Indique um tempo médio recomendado para trabalhar a região ou aplicar cada técnica.

6. Contraindicações

Informe situações em que a massagem não deve ser aplicada ou exige atenção, como:

inflamações agudas

febre

lesões recentes

trombose

infecções na pele

7. Cuidados após o atendimento

Sugira orientações simples para o cliente, como:

beber água

evitar esforço intenso logo após a sessão

realizar alongamentos leves

observar possíveis sensibilidades na região

8. Referências para estudo

Quando possível, indique livros ou materiais confiáveis sobre:

massoterapia

anatomia muscular

terapia manual

Função especial – Protocolo de massagem

Quando solicitado, gere também um PROTOCOLO DE MASSAGEM COMPLETO.

Informe:

Tempo total da sessão, por exemplo:

20 minutos

30 minutos

45 minutos

60 minutos

O protocolo deve incluir:

sequência das regiões do corpo

técnicas utilizadas em cada região

tempo aproximado em cada etapa

objetivo de cada etapa

Validação anatômica (controle de qualidade)

Antes de responder, verifique se:

os nomes dos músculos estão corretos

o nome técnico corresponde ao músculo descrito

a função do músculo está correta

a localização anatômica está correta

Evite:

misturar músculos diferentes

duplicar nomes de músculos

utilizar abreviações confusas

atribuir função de um músculo a outro

Se houver dúvida, utilize músculos amplamente conhecidos na literatura de anatomia e massoterapia.

Sempre priorize precisão anatômica e clareza didática.

Regras importantes

Não realizar diagnósticos médicos

Não substituir avaliação médica ou fisioterapêutica

As orientações devem ser educativas, responsáveis e seguras
"""

# função gerar pdf
def gerar_pdf(texto):
    arquivo = "protocolo_atendimento.pdf"
    c = canvas.Canvas(arquivo, pagesize=letter)

    y = 750
    for linha in texto.split("\n"):
        c.drawString(50, y, linha)
        y -= 20

    c.save()
    return arquivo


# INTERFACE PRINCIPAL
st.title("💆‍♂️ Assistente de Massoterapia")

st.markdown(
"""
Bem-vindo ao Assistente de Massoterapia.

Este aplicativo utiliza **IA** para ajudar massoterapeutas com:
- dúvidas técnicas
- criação de protocolos de atendimento
"""
)

st.info(
"⚠️ Este assistente não substitui avaliação médica."
)

# SIDEBAR
with st.sidebar:

    st.header("⚙️ Configurações")

    modo = st.selectbox(
        "Modo de atendimento",
        [
            "Tirar dúvidas sobre técnicas de massagem",
            "Gerar protocolo de atendimento personalizado"
        ]
    )

    modelo = st.selectbox(
        "Modelo de IA",
        [
            "openai/gpt-oss-120b"
        ]
    )
    st.markdown(
    """
    <div style="text-align: center; color: gray;">
        <hr>
        <p>Desenvolvido por Edenilson Nascimento</p>
    </div>
    """,
    unsafe_allow_html=True
)


# =========================
# MODO 1 - PERGUNTAS
# =========================

if modo == "Tirar dúvidas sobre técnicas de massagem":

    st.header("💬 Assistente de Massoterapia")

    # histórico da conversa
    if "mensagens" not in st.session_state:
        st.session_state.mensagens = []

    # mostrar histórico
    for msg in st.session_state.mensagens:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    # campo de entrada SEMPRE no final
    pergunta = st.chat_input("Digite sua dúvida sobre massoterapia")

    if pergunta:

        # mostra pergunta
        st.chat_message("user").write(pergunta)

        st.session_state.mensagens.append(
            {"role": "user", "content": pergunta}
        )

        # chamada da IA
        resposta = client.chat.completions.create(
            model=modelo,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                *st.session_state.mensagens
            ]
        )

        texto = resposta.choices[0].message.content

        # mostrar resposta
        with st.chat_message("assistant"):
            st.write(texto)

        st.session_state.mensagens.append(
            {"role": "assistant", "content": texto}
        )


# =========================
# MODO 2 - PROTOCOLO
# =========================

if modo == "Gerar protocolo de atendimento personalizado":

    st.header("📋 Gerar Protocolo de Atendimento")

    col1, col2 = st.columns(2)

    with col1:

        nome = st.text_input("Nome do cliente")

        queixa = st.text_area(
            "Queixa principal"
        )

        idade = st.number_input(
            "Idade",
            min_value=0,
            max_value=120
        )

        genero = st.selectbox(
            "Gênero",
            ["Masculino", "Feminino", "Outro"]
        )

    with col2:

        intensidade = st.selectbox(
            "Intensidade da massagem",
            ["Leve", "Moderada", "Forte"]
        )

        area = st.selectbox(
            "Área do corpo",
            [
                "Costas",
                "Pescoço",
                "Ombros",
                "Pernas",
                "Braços",
                "Cabeça",
                "Corpo inteiro"
            ]
        )

    if st.button("Gerar Protocolo"):

        prompt = f"""
Crie um protocolo profissional de massoterapia.

Dados do paciente:
Nome: {nome}
Queixa: {queixa}
Idade: {idade}
Intensidade: {intensidade}
Área afetada: {area}

Inclua:

1. avaliação inicial
2. músculos envolvidos
3. técnicas recomendadas
4. sequência de aplicação
5. duração da sessão
6. contraindicações
7. cuidados pós sessão
"""

        resposta = client.chat.completions.create(
            model=modelo,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ]
        )

        protocolo = resposta.choices[0].message.content

        st.markdown("### 📄 Protocolo sugerido")
        st.write(protocolo)

        pdf = gerar_pdf(protocolo)

        with open(pdf, "rb") as f:

            st.download_button(
                "📥 Baixar protocolo em PDF",
                f,
                file_name="protocolo_massoterapia.pdf"
            )

