import streamlit as st
import streamlit.components.v1 as components
import requests


#Configuração gerais das páginas
st.set_page_config(page_title='Pós-Tech FIAP | Datathon | Grupo 59', page_icon=":chart_with_upwards_trend:", layout= 'wide')


# SideBar
st.sidebar.title('Grupo')
st.sidebar.write('''Os :blue[__integrantes__] e suas respectivas :blue[__RM__]:''')
st.sidebar.write('''- Cheila Betina Schilling dos Santos: RM 355693
- Felipe David Abdala: RM 355751
- Lucas Coimbra Rizzo: RM 354448''')
st.sidebar.image("https://impactospositivos.com/wp-content/uploads/2024/03/FIAP-Apoiador.png", caption="Pós-Tech Data Analytics | Datathon | Grupo 59 | Imagem disponível em: vide bibliografia")

# Título Página
st.title('Conclusão')

st.info('As conclusões expostas nessa seção referem-se à execução da análise exploratória e descritiva dos relatórios de desempenho dos alunos da ONG Passos Mágicos, vide página __"Dashboard"__.')
coluna1, coluna2 = st.columns(2)
with coluna1:
    st.success('######  Dentre os principais :blue[__impactos sociais__] trazidos pelo programa destacam-se:', icon="✔️")
    st.write('''1. :green[__Aumento no conjunto do desempenho acadêmico, psicossocial e psicopedagógico (INDE):__]
    - Entre os anos de 2022 e 2024, o resultado global do __*INDE*__, envolvendo as __áreas acadêmicas, psicossociais e psicopedagógicas__ totalizaram melhoras nos alunos do programa da ONG Passos Mágicos, tanto em :blue[__escolas públicas evoluindo de 7,2 para 7,3__], quanto para :blue[__particulares migrando de 7,7 para 7,9__].
             ''')
    st.success('''2. __Aumento no conjunto do desempenho acadêmico, psicossocial e psicopedagógico (INDE):__
    - O programa tem atendido efetivamente uma demanda intrínseca aos seus valores, o de ter impacto social, conforme visto na proporção de :blue[__alunos de escola pública__] versus __de escola particulares__, sendo o primeiro grupo o mais representativo.
             ''')
with coluna2:
    st.warning('######  A partir da avaliação dos pontos a melhorar do programa, conclui-se que:', icon="⚠️")
    st.warning('''1. __Dificuldade no desempenho acadêmico:__
    - Durante os anos avaliados, identificou-se que o desempenho escolar (representado pelo "Indicador de Desempenho escolar", sigla IDA) apresentou queda quando comparados os anos de 2022 com o de 2024, tanto na média das :red[__escolas públicas, indo de 6,45 para 6,22__], quanto em :red[__escolas particulares, indo de 7,1 para 7,0__].
             ''')
    st.warning('''2. __Evasão diminuindo, porém ainda sob atenção:__
    - Em 2024, o nível de adesão alcançou em :blue[__1.054 matrículas ativas__], contra :red[__607 alunos evadindo__]. Porém, no ano anterior, 2023, com :blue[__690 matrículas ativas__] contra :red[__622 desistências__].
    - Com isso, observa-se embora o montante de alunos evadindo tenha aumentado em 2023, tivemos em 2024 uma melhora nesse quadro, representando um possível retorno de alunos que evadiram no ano anterior.
             ''')
