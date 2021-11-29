# Guia das profissões!

## Data app com informações salariais e demográficas sobre as profissões mais procuradas no Brasil.

### Visão geral do projeto

Quando eu era um estudante pré-vestibular, acompanhava o famoso **"Guia do Estudante"** - publicação da editora Abril. Esse almanaque trazia uma série de informações sobre profissões, faculdades, vestibulares e dicas de estudos. Para muitos estudantes pré-vestibular, o "Guia do Estudante" é uma valiosa fonte de informações e ajuda na escolha do curso de graduação. Sem a ambição de ser tão completo como o "Guia do Estudante", esse projeto tem como objetivo apresentar dados sobre as profissões mais buscadas pelos brasileiros. Criei, portanto, o meu próprio **"Guia das profissões"**! Clique [aqui](https://share.streamlit.io/juliompontes/profession_guide/main/app.py) para acessar o data app, que é também o produto final desse projeto.

Apesar do tom lúdico na idealização desse projeto, o seu desenvolvimento apresenta elementos importantes dos trabalhos de engenheiros e analistas de dados.

Em primeiro lugar, os dados foram obtidos diretamente de uma fonte na internet, no caso, dados da RAIS de 2019, disponibilizados pelo Ministério da Economia [nesse endereço](ftp://ftp.mtps.gov.br/pdet/microdados/RAIS/2019/). A coleta dos dados foi realizada através de um script shell - arquivo "collect_data.sh". Esse script **automatiza** os seguintes processos:

1. download dos 6 arquivos de interesse para o projeto localizados no endereço mencionado acima;
2. descompactação dos 6 arquivos, movendo-os para o diretório correto (também criado através do shell script); e
3. remoção de diretórios desnecessários para o projeto.

Após a execução do script shell, temos os arquivos de dados em formato ".txt" prontos para serem lidos. No entanto, os 6 arquivos no formato ".txt" totalizam 32,5 GB. Com esse tamanho dos arquivos, métodos mais comuns de leitura são insuficientes. Para resolver esse problema, lancei mão de uma ferramenta chamada [Dask](https://docs.dask.org/en/stable/). Dask é uma biblioteca para **computação paralela** em Python. Em outras palavras, Dask é uma ótima ferramenta para ajudar a processar dados maiores que a memória, ao aumentar o tamanho de todos os núcleos em uma única máquina ou a expandir os núcleos em um cluster, funcionando muito bem em uma única máquina e de forma mais leve que Spark, por exemplo.

Dask permite que os arquivos sejam lidos em um formato análogo a um dataframe do pandas. Dessa forma, é possível realizar algumas transformações nos dados antes de carregá-los para a memória do computador. No jupyter notebook "data_preparation.ipynb" são removidas as linhas do dataframe que não serão utilizadas, pois se referem a profissões que não são de interesse nesse projeto. Com um dataset mais leve, os dados estão prontos para serem carregados como um dataframe pandas. Ainda no mesmo jupyter notebook, a preparação dos dados segue até chegar aos datasets finais, que serão utilizados para criar o data app.

Até esse ponto, o projeto executou um processo de ETL - extração, tranformação e carregamento (load) de dados. Com os dados prontos, o arquivo "app.py" constrói o data app. 

O data app é construído através do [Streamlit](https://streamlit.io/), um framework open-source que transforma scripts python em web apps compartilháveis. 

O data app consiste em uma caixa de seleção onde é possível escolher uma das profissões listadas e na apresentação de uma série de informações - salariais e demográficas - sobre a profissão escolhida. Para dispor tais informações, foram criados gráficos - barras, histograma e de pizza, por exemplo - através da biblioteca **plotly**.

Com o data app pronto e os arquivos enviados para o repositório no github, o Streamlit permite o deploy de maneira extremamente simples. É só indicar o repositório do github e o arquivo com extensão ".py" em que o data app foi criado que, se não houver nenhum problema, o Streamlit cria um link compartilhável com o data app pronto para ser utilizado!

### Como esse projeto pode ser aplicado para resolver um problema?

O projeto do "Guia das profissões" tem vários elementos em seu desenvolvimento com potencial para resolver diversos problemas que as áreas de dados das empresas encontram no dia-a-dia.

- Obtenção de dados: já é um clichê a frase "dado é o novo petróleo". E existe uma quantidade quase infinita de dados disponíveis atualmente, com essa quantidade crescendo expoencialmente a cada dia. Mas tão importante quanto a quantidade de dados é a capacidade de coletá-los e disponibilizá-los para uso. Esses são alguns dos desafios enfrentados pelos engenheiros de dados nas empresas: coletar dados de forma sustentável, realizar as transformações necessárias, armazenar os dados adequadamente - tendo em vista limitações de orçamento, capacidade das máquinas e outras - e disponibilizar os dados para cientistas e analistas. Quase todo esse pipeline de dados é realizado nesse projeto de forma relativamente simples, mas que cumpre o objetivo.

- Leitura de dados a partir de grandes arquivos: lidar com arquivos na escala de giga e terabytes é um outro desafio. Existem diversas soluções para esse problema, desde a transformação dos arquivos em formatos mais leves até a utilização de computação distribuída. Cada problema exige um tipo de solução específica, as vezes com combinações de soluções. Esse projeto tinha como problema a leitura de arquivos que somavam mais de 30GB. Para realizar a leitura e fazer as transformações iniciais no dataset antes de carregá-lo na memória da máquina foi utilizado o **Dask**, uma biblioteca para computação paralela, que se mostrou eficiente para resolver esse problema específico do projeto. 

- Produtizição através de data app: é muito comum no mundo de dados ver a construção de dashboards, modelos de Machine Learning e outras soluções que, no final das contas, não entregam nenhum produto concreto. O data app é uma opção, dentre várias outras, para entregar uma solução mais concreta do trabalho realizado.

### Tecnologias

- [x] **Shell script** para baixar, descompactar e mover os arquivos com os dados para o diretório correto
- [x] Python - bibliotecas **Dask** para ler e manipular grandes arquivos; **Pandas** e **Numpy** para trabalhar com a transformação dos dados; **Plotly** para gerar as visualizações
- [x] **Jupyter Notebook** para realizar a preparação dos dados
- [x] **Streamlit** para desenvolver o data app

### No que você deve ficar de olho :eyes:

* :bulb: Execução de todo o **roadmap de um projeto de dados**: coleta, transformação, leitura, análise, visualização e deploy
* :mechanical_arm: Download, descompactação, transformação e leitura automatizada de uma base de dados pública de tamanho considerável (os 6 arquivos no formato ".txt" totalizaram 32,5 GB)
* :chart_with_upwards_trend: **Dashboard** com dados salariais e demográficos das profissões no Brasil em um data app interativo e compartilhável  

### Por que realizar esse projeto?

Além da motivação lúdica de relembrar um material importante da minha época de estudante e criar algo relacionado, **esse projeto apresenta todo o roadmap de um projeto de dados: a coleta de dados públicos, transformação e leitura do dataset, análise das informações,  criação de visualizações dos dados e deploy**. Para isso, diversas soluções foram experimentadas até que o resultado final fosse alcançado. Foram testados scripts python e shell para o download dos dados, tecnologias diferentes para a leitura dos arquivos (pyspark, databricks, dask e outros), criação de um banco de dados, bibliotecas de visualização de dados (plotly, seaborn, altair, matplotlib e outros) e frameworks para criação de data apps (streamlit, dash, datapane, etc).

Além da entrega do data app, esse projeto foi uma excelente oportunidade de estudar tecnologias diversas para diferentes etapas do roadmap do trabalho com dados, abrindo novas possibilidades de projetos e ampliando a minha caixa de ferramentas. 

### Como executar esse projeto

1. executar o arquivo do tipo shell "collect_data.sh" para fazer o download, descompactar e mover os arquivos com os dados;
2. executar o jupyter notebook "data_preparation.ipynb" para preparar os datasets que serão utlizados no desenvolvimento do data app;
3. executar o arquivo python "app.py" para criar o data app.
