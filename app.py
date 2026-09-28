import streamlit as st
import pandas as pd
import os

# =========================================================
# CONFIGURAÇÃO DA PÁGINA
# =========================================================

st.set_page_config(
    page_title="HairStore PRO",
    page_icon="💇‍♀️",
    layout="wide",
    initial_sidebar_state="expanded"
)

ARQUIVO = "produtos_cabelo.csv"


# =========================================================
# IMAGENS
# =========================================================

IMAGEM_HERO = (
    "https://images.unsplash.com/"
    "photo-1522337360788-8b13dee7a37e"
    "?auto=format&fit=crop&w=1800&q=90"
)

IMAGEM_LOJA = (
    "https://images.unsplash.com/"
    "photo-1556229010-6c3f2c9ca5f8"
    "?auto=format&fit=crop&w=1200&q=85"
)


# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

@import url(
'https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap'
);

/* =========================================================
FONTE
========================================================= */

html,
body,
[class*="css"] {
    font-family: 'Poppins', sans-serif;
}


/* =========================================================
FUNDO PRINCIPAL
========================================================= */

.stApp {
    background:
        linear-gradient(
            135deg,
            #F7F1F0 0%,
            #E9DDE0 50%,
            #DCC9D0 100%
        );
}


/* =========================================================
ÁREA PRINCIPAL
========================================================= */

.block-container {
    max-width: 1400px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}


/* =========================================================
SIDEBAR
========================================================= */

[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            #35242D,
            #513541
        );

    border-right:
        2px solid #C78B9F;
}

[data-testid="stSidebar"] * {
    color: #FFFFFF !important;
}


/* =========================================================
LOGO
========================================================= */

.logo-title {
    font-size: 28px;
    font-weight: 800;
    color: #FFFFFF !important;
    margin-bottom: 5px;
}

.logo-subtitle {
    font-size: 11px;
    font-weight: 700;
    color: #E7B9C7 !important;
    letter-spacing: 1px;
}


/* =========================================================
TÍTULOS
========================================================= */

.page-title {
    font-size: 38px;
    font-weight: 800;
    color: #35242D !important;
    margin-bottom: 5px;
}

.page-subtitle {
    font-size: 17px;
    color: #604A53 !important;
    margin-bottom: 30px;
}


/* =========================================================
HERO
========================================================= */

.hero-container {
    position: relative;
    height: 430px;
    width: 100%;
    border-radius: 28px;
    overflow: hidden;
    margin-bottom: 35px;

    background-size: cover;
    background-position: center;

    box-shadow:
        0 15px 35px rgba(0,0,0,0.22);
}

.hero-overlay {
    position: absolute;
    inset: 0;

    background:
        linear-gradient(
            90deg,
            rgba(53,36,45,0.97) 0%,
            rgba(53,36,45,0.82) 45%,
            rgba(53,36,45,0.15) 100%
        );
}

.hero-content {
    position: absolute;
    top: 50%;
    left: 7%;

    transform: translateY(-50%);

    max-width: 580px;
}

.hero-number {
    font-size: 70px;
    font-weight: 800;
    color: #E5A9BC !important;
    line-height: 1;
}

.hero-title {
    font-size: 46px;
    font-weight: 800;
    color: #FFFFFF !important;

    margin-top: 12px;
    line-height: 1.1;
}

.hero-text {
    font-size: 17px;
    color: #F5E8EC !important;

    margin-top: 20px;
    line-height: 1.7;
}

.hero-badge {
    display: inline-block;

    margin-top: 24px;

    padding: 10px 22px;

    border-radius: 30px;

    background: #A95F79;

    color: #FFFFFF !important;

    font-size: 14px;
    font-weight: 700;
}


/* =========================================================
CARDS
========================================================= */

.info-card {
    background: #FFFFFF;

    border-radius: 22px;

    padding: 28px;

    min-height: 170px;

    border:
        1px solid rgba(169,95,121,0.30);

    box-shadow:
        0 10px 25px rgba(0,0,0,0.08);
}

.card-icon {
    font-size: 32px;
}

.card-number {
    font-size: 34px;
    font-weight: 800;

    color: #35242D !important;

    margin-top: 10px;
}

.card-label {
    font-size: 14px;
    font-weight: 700;

    color: #725D66 !important;

    margin-top: 5px;
}


/* =========================================================
CARD ESCURO
========================================================= */

.dark-card {
    background:
        linear-gradient(
            135deg,
            #35242D,
            #513541
        );

    border-radius: 24px;

    padding: 30px;

    box-shadow:
        0 12px 30px rgba(0,0,0,0.16);
}

.dark-card h2 {
    color: #FFFFFF !important;
    margin-top: 0;
}

.dark-card p {
    color: #F0E2E7 !important;
    line-height: 1.7;
}


/* =========================================================
FORMULÁRIO
========================================================= */

[data-testid="stForm"] {
    background:
        rgba(255,255,255,0.88);

    padding: 30px;

    border-radius: 25px;

    border:
        1px solid #D3A9B6;

    box-shadow:
        0 10px 30px rgba(0,0,0,0.08);
}


/* =========================================================
LABELS
========================================================= */

[data-testid="stWidgetLabel"],
[data-testid="stWidgetLabel"] label,
[data-testid="stWidgetLabel"] p,
[data-testid="stWidgetLabel"] span,
.stTextInput label,
.stNumberInput label,
.stSelectbox label,
.stTextArea label {
    color: #35242D !important;

    opacity: 1 !important;

    font-size: 15px !important;

    font-weight: 700 !important;
}


/* =========================================================
INPUTS
========================================================= */

.stTextInput input,
.stNumberInput input,
.stTextArea textarea {
    background-color: #FFFFFF !important;

    color: #30252A !important;

    -webkit-text-fill-color:
        #30252A !important;

    border:
        2px solid #B78395 !important;

    border-radius: 12px !important;

    font-size: 16px !important;

    font-weight: 500 !important;
}

.stTextInput input:focus,
.stNumberInput input:focus,
.stTextArea textarea:focus {
    border:
        2px solid #A95F79 !important;

    box-shadow:
        0 0 0 3px rgba(169,95,121,0.15) !important;
}

input::placeholder,
textarea::placeholder {
    color: #77666D !important;
    opacity: 1 !important;
}


/* =========================================================
SELECTBOX
========================================================= */

[data-baseweb="select"] > div {
    background-color: #393039 !important;

    border:
        2px solid #9E687C !important;

    border-radius: 12px !important;
}

[data-baseweb="select"] > div * {
    color: #FFFFFF !important;

    -webkit-text-fill-color:
        #FFFFFF !important;

    opacity: 1 !important;
}

[data-baseweb="select"] input {
    color: #FFFFFF !important;

    -webkit-text-fill-color:
        #FFFFFF !important;
}

[data-baseweb="select"] [class*="singleValue"] {
    color: #FFFFFF !important;
}

[data-baseweb="select"] svg {
    fill: #FFFFFF !important;
    color: #FFFFFF !important;
}

[data-baseweb="select"] > div:hover {
    border-color: #D79AAF !important;
}


/* =========================================================
MENU SELECTBOX
========================================================= */

[data-baseweb="popover"] {
    background-color: #393039 !important;
}

[data-baseweb="menu"] {
    background-color: #393039 !important;
}

[role="option"] {
    background-color: #393039 !important;

    color: #FFFFFF !important;

    -webkit-text-fill-color:
        #FFFFFF !important;
}

[role="option"]:hover {
    background-color: #704658 !important;

    color: #FFFFFF !important;
}


/* =========================================================
BOTÕES
========================================================= */

.stButton > button,
div[data-testid="stFormSubmitButton"] > button {
    background:
        linear-gradient(
            135deg,
            #8F4E67,
            #B86F88
        ) !important;

    color: #FFFFFF !important;

    border: none !important;

    border-radius: 14px !important;

    min-height: 54px;

    font-family:
        'Poppins', sans-serif !important;

    font-size: 15px !important;

    font-weight: 700 !important;

    box-shadow:
        0 8px 18px rgba(143,78,103,0.25);
}

.stButton > button:hover,
div[data-testid="stFormSubmitButton"] > button:hover {
    background:
        linear-gradient(
            135deg,
            #713B50,
            #98566F
        ) !important;

    color: #FFFFFF !important;

    transform:
        translateY(-1px);
}


/* =========================================================
TABELA
========================================================= */

[data-testid="stDataFrame"] {
    background: #FFFFFF;

    border-radius: 18px;

    overflow: hidden;

    border:
        1px solid #D3A9B6;
}


/* =========================================================
RODAPÉ
========================================================= */

.footer {
    margin-top: 50px;

    text-align: center;

    color: #705863 !important;

    font-size: 14px;

    font-weight: 600;
}


/* =========================================================
RESPONSIVO
========================================================= */

@media (max-width: 768px) {

    .hero-container {
        height: 500px;
    }

    .hero-content {
        left: 8%;
        right: 8%;
    }

    .hero-title {
        font-size: 34px;
    }

    .hero-number {
        font-size: 55px;
    }

    .page-title {
        font-size: 30px;
    }
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# FUNÇÕES
# =========================================================

def carregar_dados():

    colunas = [
        "Marca",
        "Produto",
        "Categoria",
        "Tipo de Cabelo",
        "Tamanho",
        "Estoque",
        "Valor",
        "Observações"
    ]

    if os.path.exists(ARQUIVO):

        try:

            dados = pd.read_csv(ARQUIVO)

            return dados

        except Exception:

            return pd.DataFrame(columns=colunas)

    return pd.DataFrame(columns=colunas)


def salvar_dados(dados):

    dados.to_csv(
        ARQUIVO,
        index=False
    )


# =========================================================
# CARREGAR DADOS
# =========================================================

df = carregar_dados()


# Garantir colunas necessárias

colunas_necessarias = [
    "Marca",
    "Produto",
    "Categoria",
    "Tipo de Cabelo",
    "Tamanho",
    "Estoque",
    "Valor",
    "Observações"
]

for coluna in colunas_necessarias:

    if coluna not in df.columns:

        df[coluna] = ""


# Converter valores

df["Valor"] = pd.to_numeric(
    df["Valor"],
    errors="coerce"
).fillna(0)

df["Estoque"] = pd.to_numeric(
    df["Estoque"],
    errors="coerce"
).fillna(0)


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.markdown(
"""
<div class="logo-title">
💇‍♀️ HairStore
</div>

<div class="logo-subtitle">
BELEZA E CUIDADOS CAPILARES
</div>
""",
    unsafe_allow_html=True
)

st.sidebar.markdown("<br>", unsafe_allow_html=True)


menu = st.sidebar.radio(
    "NAVEGAÇÃO",
    [
        "🏠 Dashboard",
        "➕ Cadastrar Produto",
        "🛍️ Produtos Cadastrados"
    ]
)


st.sidebar.markdown("---")

st.sidebar.caption(
    "HairStore PRO • 2026"
)


# =========================================================
# DASHBOARD
# =========================================================

if menu == "🏠 Dashboard":

    st.markdown(
f"""
<div class="hero-container"
style="background-image: url('{IMAGEM_HERO}');">

<div class="hero-overlay"></div>

<div class="hero-content">

<div class="hero-number">
01.
</div>

<div class="hero-title">
Seu cabelo.<br>
Seu cuidado.
</div>

<div class="hero-text">
Tenha todos os seus produtos de cabelo organizados em um
único lugar. Cadastre, consulte e acompanhe seu estoque
de forma simples, rápida e profissional.
</div>

<div class="hero-badge">
✨ BELEZA INTELIGENTE
</div>

</div>

</div>
""",
        unsafe_allow_html=True
    )

    st.markdown(
"""
<div class="page-title">
📊 Visão geral da sua loja
</div>

<div class="page-subtitle">
Acompanhe seus produtos e mantenha seu estoque organizado.
</div>
""",
        unsafe_allow_html=True
    )

    total_produtos = len(df)

    valor_total = (
        df["Valor"] * df["Estoque"]
    ).sum()

    estoque_total = df["Estoque"].sum()


    col1, col2, col3 = st.columns(3)


    with col1:

        st.markdown(
f"""
<div class="info-card">

<div class="card-icon">
🧴
</div>

<div class="card-number">
{total_produtos}
</div>

<div class="card-label">
PRODUTOS CADASTRADOS
</div>

</div>
""",
            unsafe_allow_html=True
        )


    with col2:

        st.markdown(
f"""
<div class="info-card">

<div class="card-icon">
💰
</div>

<div class="card-number">
R$ {valor_total:,.2f}
</div>

<div class="card-label">
VALOR TOTAL DO ESTOQUE
</div>

</div>
""",
            unsafe_allow_html=True
        )


    with col3:

        st.markdown(
f"""
<div class="info-card">

<div class="card-icon">
📦
</div>

<div class="card-number">
{estoque_total:,.0f}
</div>

<div class="card-label">
ITENS EM ESTOQUE
</div>

</div>
""",
            unsafe_allow_html=True
        )


    st.markdown("<br>", unsafe_allow_html=True)


    coluna1, coluna2 = st.columns([1.1, 1])


    with coluna1:

        st.markdown(
"""
<div class="dark-card">

<h2>
✨ Beleza organizada
</h2>

<p>
O HairStore PRO permite manter todos os seus produtos
capilares organizados em um único lugar.
</p>

<p>
Cadastre shampoos, máscaras, condicionadores, óleos,
finalizadores e muito mais.
</p>

</div>
""",
            unsafe_allow_html=True
        )


    with coluna2:

        st.image(
            IMAGEM_LOJA,
            use_container_width=True
        )


# =========================================================
# CADASTRAR PRODUTO
# =========================================================

elif menu == "➕ Cadastrar Produto":

    st.markdown(
"""
<div class="page-title">
➕ Novo produto
</div>

<div class="page-subtitle">
Adicione um novo produto à sua loja de cabelos.
</div>
""",
        unsafe_allow_html=True
    )


    with st.form(
        "cadastro_produto",
        clear_on_submit=True
    ):

        col1, col2 = st.columns(2)


        with col1:

            marca = st.text_input(
                "🏷️ Marca"
            )

            produto = st.text_input(
                "🧴 Nome do Produto"
            )

            categoria = st.selectbox(
                "📂 Categoria",
                [
                    "Shampoo",
                    "Condicionador",
                    "Máscara de Tratamento",
                    "Creme para Pentear",
                    "Leave-in",
                    "Óleo Capilar",
                    "Finalizador",
                    "Protetor Térmico",
                    "Tônico Capilar",
                    "Gel",
                    "Pomada",
                    "Kit",
                    "Outro"
                ]
            )

            tipo_cabelo = st.selectbox(
                "💇 Tipo de Cabelo",
                [
                    "Todos os tipos",
                    "Liso",
                    "Ondulado",
                    "Cacheado",
                    "Crespo",
                    "Seco",
                    "Oleoso",
                    "Misto",
                    "Danificado",
                    "Colorido"
                ]
            )


        with col2:

            tamanho = st.text_input(
                "📏 Tamanho / Volume",
                placeholder="Ex.: 300 ml"
            )

            estoque = st.number_input(
                "📦 Quantidade em Estoque",
                min_value=0,
                value=0,
                step=1
            )

            valor = st.number_input(
                "💰 Preço do Produto",
                min_value=0.0,
                value=0.0,
                step=1.0
            )

            observacoes = st.text_area(
                "📝 Observações"
            )


        cadastrar = st.form_submit_button(
            "💾 CADASTRAR PRODUTO"
        )


    if cadastrar:

        if (
            marca.strip()
            and produto.strip()
        ):

            novo_produto = pd.DataFrame(
                [{
                    "Marca": marca.strip(),
                    "Produto": produto.strip(),
                    "Categoria": categoria,
                    "Tipo de Cabelo": tipo_cabelo,
                    "Tamanho": tamanho.strip(),
                    "Estoque": int(estoque),
                    "Valor": float(valor),
                    "Observações": observacoes.strip()
                }]
            )


            df = pd.concat(
                [
                    df,
                    novo_produto
                ],
                ignore_index=True
            )


            salvar_dados(df)


            st.success(
                "🧴 Produto cadastrado com sucesso!"
            )


            st.rerun()


        else:

            st.warning(
                "⚠️ Preencha Marca e Nome do Produto."
            )


# =========================================================
# PRODUTOS CADASTRADOS
# =========================================================

elif menu == "🛍️ Produtos Cadastrados":

    st.markdown(
"""
<div class="page-title">
🛍️ Minha loja
</div>

<div class="page-subtitle">
Consulte e pesquise todos os produtos cadastrados.
</div>
""",
        unsafe_allow_html=True
    )


    if df.empty:

        st.markdown(
"""
<div class="dark-card">

<h2>
🧴 Nenhum produto cadastrado
</h2>

<p>
Sua loja ainda está vazia.
Cadastre seu primeiro produto para começar.
</p>

</div>
""",
            unsafe_allow_html=True
        )


    else:

        busca = st.text_input(
            "🔎 Pesquisar produto",
            placeholder="Digite marca, produto, categoria ou tipo de cabelo..."
        )


        if busca:

            mascara = (
                df.astype(str)
                .apply(
                    lambda coluna:
                    coluna.str.contains(
                        busca,
                        case=False,
                        na=False
                    )
                )
                .any(axis=1)
            )

            df_filtrado = df[mascara]

        else:

            df_filtrado = df


        st.dataframe(
            df_filtrado,
            use_container_width=True,
            hide_index=True
        )


        st.markdown("<br>", unsafe_allow_html=True)


        opcoes_produtos = df.index.tolist()


        produto_excluir = st.selectbox(
            "🗑️ Selecione um produto para excluir",
            options=opcoes_produtos,
            format_func=lambda indice:
                f"{df.loc[indice, 'Marca']} "
                f"{df.loc[indice, 'Produto']} - "
                f"{df.loc[indice, 'Categoria']}"
        )


        if st.button(
            "🗑️ EXCLUIR PRODUTO"
        ):

            df = df.drop(
                produto_excluir
            )

            df = df.reset_index(
                drop=True
            )


            salvar_dados(df)


            st.success(
                "🧴 Produto excluído com sucesso!"
            )


            st.rerun()


# =========================================================
# RODAPÉ
# =========================================================

st.markdown(
"""
<div class="footer">

💇‍♀️ HairStore PRO<br>
Beleza e cuidados capilares

</div>
""",
    unsafe_allow_html=True
)
