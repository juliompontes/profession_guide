import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(layout="wide")

df_salary = pd.read_csv('app_datasets/salary.csv')
df_age = pd.read_csv('app_datasets/age.csv')
df_gender = pd.read_csv('app_datasets/gender.csv')
df_local = pd.read_csv('app_datasets/local.csv')

row1, row2 = st.columns(2)

with row1:
    st.title("Guia das profissões")
    st.subheader("Data app sobre as profissões mais procuradas no Brasil")

with row2:
    st.markdown("")
    st.markdown("")
    st.markdown("Esse data app utiliza dados da **RAIS** (Relação Anual de Informações Sociais) do ano de **2019** - "
                "disponibilizados pelo Ministério da Economia do Brasil - e tem como objetivo apresentar um panorama geral de algumas das profissões mais procuradas no Brasil. "
                "Para tanto, são apresentados dados **salariais** e **demográficos** das profissões selecionadas.")

profissoes_lista = df_salary['Profissão'].unique()
profissao = st.selectbox("Escolha uma profissão:", profissoes_lista)

st.header("Dados salariais")

fig_ind_mean = go.Figure(go.Indicator(
    value = df_salary[df_salary['Profissão']==profissao]['Remuneração (em R$)'].mean(),
    number = {'prefix': "R$"},
    domain = {'x': [0, 1], 'y': [0, 1]},
    title= {'text': "Salário médio"}))

fig_ind_mean.update_layout(font_family="Rockwell",
                           width=282,
                           height=90,
                           paper_bgcolor="#edebeb",
                           plot_bgcolor="#c5c7c9",
                           font_color="black",
                           margin_b=10,
                           margin_l=20,
                           margin_r=20,
                           margin_t=35
                           )

fig_ind_mean.update_traces(title_font_color="black",
                           title_font_family="Rockwell",
                           title_font_size=16,
                           number_font_family="Rockwell",
                           number_font_size=40,
                           number_valueformat="fmt"
                           )

fig_ind_med = go.Figure(go.Indicator(
    value = df_salary[df_salary['Profissão']==profissao]['Remuneração (em R$)'].quantile(q=0.5),
    number = {'prefix': "R$"},
    domain = {'x': [0, 1], 'y': [0, 1]},
    title= {'text': "50% dos profissionais ganham até"}))

fig_ind_med.update_layout(font_family="Rockwell",
                          width=282,
                          height=90,
                          paper_bgcolor="#edebeb",
                          plot_bgcolor="#c5c7c9",
                          font_color="black",
                          margin_b=10,
                          margin_l=20,
                          margin_r=20,
                          margin_t=35
                          )

fig_ind_med.update_traces(title_font_color="black",
                          title_font_family="Rockwell",
                          title_font_size=16,
                          number_font_family="Rockwell",
                          number_font_size=40,
                          number_valueformat="fmt"
                          )

fig_ind_quantile3 = go.Figure(go.Indicator(
    value = df_salary[df_salary['Profissão']==profissao]['Remuneração (em R$)'].quantile(q=0.75),
    number = {'prefix': "R$"},
    domain = {'x': [0, 1], 'y': [0, 1]},
    title= {'text': "75% dos profissionais ganham até"}))

fig_ind_quantile3.update_layout(font_family="Rockwell",
                                width=282,
                                height=90,
                                paper_bgcolor="#edebeb",
                                plot_bgcolor="#c5c7c9",
                                font_color="black",
                                margin_b=10,
                                margin_l=20,
                                margin_r=20,
                                margin_t=35
                                )

fig_ind_quantile3.update_traces(title_font_color="black",
                                title_font_family="Rockwell",
                                title_font_size=16,
                                number_font_family="Rockwell",
                                number_font_size=40,
                                number_valueformat="fmt"
                                )

fig_ind_max = go.Figure(go.Indicator(
    value = df_salary[df_salary['Profissão']==profissao]['Remuneração (em R$)'].max(),
    number = {'prefix': "R$"},
    domain = {'x': [0, 1], 'y': [0, 1]},
    title= {'text': "Salário máximo"}))

fig_ind_max.update_layout(font_family="Rockwell",
                          width=282,
                          height=90,
                          paper_bgcolor="#edebeb",
                          plot_bgcolor="#c5c7c9",
                          font_color="black",
                          margin_b=10,
                          margin_l=20,
                          margin_r=20,
                          margin_t=35
                          )

fig_ind_max.update_traces(title_font_color="black",
                          title_font_family="Rockwell",
                          title_font_size=16,
                          number_font_family="Rockwell",
                          number_font_size=40,
                          number_valueformat="fmt"
                          )

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.plotly_chart(fig_ind_mean)

with col2:
    st.plotly_chart(fig_ind_med)
    
with col3:
    st.plotly_chart(fig_ind_quantile3)
    
with col4:
    st.plotly_chart(fig_ind_max)
    
# Construindo o gráfico de barras com os salários médios
df_salary_mean = pd.DataFrame(df_salary.groupby(['Profissão'])['Remuneração (em R$)'].mean().sort_values(ascending=True))
df_salary_mean.reset_index(inplace=True)
fig_comparative = px.bar(df_salary_mean.round(2),
    x='Remuneração (em R$)',
    y='Profissão',
    text='Remuneração (em R$)',
    orientation='h')

fig_comparative.update_layout(font_family="Rockwell",
                              width=586,
                              height=550,
                              paper_bgcolor="#edebeb",
                              plot_bgcolor="#c5c7c9",
                              font_color="black",
                              margin_b=20,
                              margin_l=20,
                              margin_r=20,
                              margin_t=30                         
)

fig_comparative.update_traces(marker_color="#ffbb00",
                              textfont_color="black"                              
)

# Construindo o histograma com a distribuição dos salários
fig_salario = px.histogram(df_salary[df_salary['Profissão'] == profissao],
    x='Remuneração (em R$)',
    nbins=15,
    histnorm="percent"
)

fig_salario.update_yaxes(title_text="Porcentagem",
                         ticksuffix="%", 
                         showgrid=True)

fig_salario.update_traces(opacity=0.7,
                          marker_color="#00008b")

fig_salario.update_layout(font_family="Rockwell",
                          width=586,
                          height=550,
                          paper_bgcolor="#edebeb",
                          plot_bgcolor="#c5c7c9",
                          font_color="black",
                          margin_b=20,
                          margin_l=20,
                          margin_r=20,
                          margin_t=30                                                    
)

# Exibindo os gráficos de salários em duas colunas
col1, col2 = st.columns(2)

with col1:
    st.subheader("Salário médio por profissão (em R$)")
    st.plotly_chart(fig_comparative)
    st.markdown("O gráfico acima mostra os salários médios de todas as profissões selecionadas para esse estudo. "
                "O objetivo dessa visualização é gerar um quadro comparativo geral entre os salários médios das diferentes profissões.")

with col2:
    st.subheader("Distribuição dos salários")
    st.plotly_chart(fig_salario)
    st.write("O gráfico acima mostra a distribuição - em termos relativos (%) - dos salários dos profisisonais da área escolhida. "
             "Com essa visualização é possível observar as faixas salariais da maioria dos profissionais. "
             "Ao mover o cursor sobre uma barra, você conseguirá ver a faixa salarial e a porcentagem de profissionais que se encontra nessa faixa.") 

st.header("Dados demográficos")

# Criando o gráfico de barras com as faixas etárias
fig_age = px.histogram(df_age[df_age['Profissão'] == profissao],
    x='Faixa Etária',
    histnorm="percent")

fig_age.update_traces(marker_color="#ffbb00")

fig_age.update_yaxes(title_text="Porcentagem",
                     ticksuffix="%",
                     showgrid=True)

fig_age.update_layout(font_family="Rockwell",
                          width=586,
                          height=550,
                          paper_bgcolor="#edebeb",
                          plot_bgcolor="#c5c7c9",
                          font_color="black",
                          margin_b=20,
                          margin_l=20,
                          margin_r=20,
                          margin_t=30                                                    
)

# Criando o gráfico de pizza com os gêneros
fig_gender = px.pie(df_gender[df_gender['Profissão'] == profissao],
    names = 'Gênero',
    color = 'Gênero',
    color_discrete_map={'Masculino':'#8bb598',
                        'Feminino':'#ff9494'}
)

fig_gender.update_traces(textfont_color="black",
                         textfont_family="Rockwell",
                         textfont_size=24)

fig_gender.update_layout(legend_font_family="Rockwell",
                         legend_font_size=20,
                         legend_orientation="h",
                         legend_x=0.5,
                         legend_y=1.1,
                         legend_xanchor="center",
                         legend_yanchor="top",
                         width=586,
                         height=550,
                         paper_bgcolor="#edebeb",
                         plot_bgcolor="#c5c7c9",
                         font_color="black",
                         margin_b=20,
                         margin_l=20,
                         margin_r=20,
                         margin_t=30                                                    
)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Faixa etária")
    st.plotly_chart(fig_age)
    st.markdown("Com essa visuzalição é possível observar as faixas etárias dos profissionais da área escolhida. "
                "Com o cursor sobre a barra, você conseguirá ver a faixa etária e a porcentagem de profissionais que se encontra nessa faixa.")

with col2:
    st.subheader("Gênero dos profissionais")
    st.plotly_chart(fig_gender)
    st.markdown("O famoso gráfico de pizza acima apresenta a proporção de homens e mulheres - únicas respostas encontradas no dataset da RAIS - "
                "dentro da área profissional selecionada.")
