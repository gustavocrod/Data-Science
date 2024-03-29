## NumPy

É engraçado o fato de que uma parte considerável dos módulos feitos para linguagem Python tem "py" no nome, assim como é o "JS" para JavaScript, e bom, o NumPy aparentemente não é uma exceção. Bom, e o que diabos seria esse tal de NumPy? A sigla é um acrônico para *Numerical Python*, ou seja, fornece suporte para **manipulações numéricas** em Python. A estrutura principal do NumPy é um carinha chamado **array**, que se você vem de outras linguagens, provavelmente está familiarizado com esse nome, se não, pode-se dizer que o array é um parente próximo da estrutura de listas. Talvez você que esteja lendo isso, como ótimo(a) observador(a) que é, pode estar se perguntando: ok mas tipo, se já temos um "array" em Python que são as listas, por que *krai* precisamos de outra estrutura como essa? 

<p align="center">
  <img src="https://i.pinimg.com/236x/82/ae/00/82ae008d189fc10463d8621b60bbb9a0.jpg">
</p>

Certo, acontece que, para operações matemáticas em larga escala ou processos de inteligência artificial, listas podem se mostrar bastantes ineficientes e facilmente travando seu PC que custou 10 pau. Felizmente, algumas almas caridosas perceberam essa demanda por **eficiência no processamento** e criaram algumas bibliotecas para nós, meros mortais. NumPy, assim como outras bibliotecas utilizadas para ciência de dados, foi **escrito em C/C++**, ou seja, como são linguagens mais "próximas ao hardware" o ganho de performance é muito maior do que utilizando estruturas de dados padrão do Python.

## Hora do Dale (ou quase)

Ok, com essa breve introdução ao NumPy, podemos logo pôr a mão na massa e entender como esse negócio funciona de verdade. Assim como seu amiguinho main yasuo assiste 10 vídeos por dia do [courtesy](https://www.youtube.com/channel/UCLGbbmMi8cREKZ_SSZR9ORQ) e ainda assim *feeda* no seu game, não conseguiremos realmente aprender nada novo sem realmente **treinar e praticar!** Por isso, você que se interessou por esta série de tutoriais está convidado(a) a não apenas seguir os passos feitos aqui, como também alterá-los e descobrir por si só o leque de possibilidades que se abriu. 

Partindo do pressuposto que o Python já está instalado na sua máquina, juntamente com o gerenciador de pacotes (pip), instalar o NumPy é mais fácil que jogar de Master Yi no Ferro IV. Recomendamos fortemente a instalação do ambiente interativo Jupyter, que facilitará muito seus estudos.

*NOTA: Não compactuamos com instalação diretamente por anaconda pois aqui é raiz.

### Passo 1: Instalar o Jupyter Lab
```
$ pip install jupyterlab
```

### Passo 2: Instalar o NumPy
```
$ pip install numpy
```

### Passo 3: Ir até o diretório desejado, e abrir uma sessão do Jupyter, digitando:
```
$ jupyter lab
```

## Agora sim, Hora do Dale <img src="https://3.bp.blogspot.com/-weDqm5JxCWQ/VdDtk2WvvSI/AAAAAAAAGh0/7PdkJ_r4ojw/s1600/image%2B187.png" width="50" height="40" >

Estamos com tudo preparado para começar a praticar esse tal de Numpy. Let's bora!!

A primeira coisa que devemos fazer para utilizar um módulo, assim como em toda linguagem de programação que se preze, é a importação. É importante destacarmos o uso do `as`. Para não precisarmos escrever `numpy` toda vez que quisermos utilizá-lo, podemos dar um apelido a ele que, por convenção, é chamado de np.
```
import numpy as np
```
Após isso, estamos "autorizados" a começar a utilizar as funcionalidades do pacote. Você pode começar com o comando `help(np.array)` para ler mais sobre ele, mas não fazemos isso aqui.

<p align="center">
  <img src="https://pbs.twimg.com/media/EBdCJqfW4AAdyir.jpg" height=200>
</p>

Vamos começar logo esta jornada criando um array simples. Existem diferentes formas de criá-lo e vamos ver algumas delas; a primeira é através de um limite (*range*, sacou né!?) de valores.
```
array1 = np.arange(15)
output: array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
```
Nos foi retornado um array de 0 até 14, ou seja, um array com 15 elementos. Ao passarmos **apenas um parâmetro** para a função `arange()`, a mesma entende que este é o seu limite excludente, ou seja, irá parar no elemento - 1, sendo 0 o padrão para o início. Podemos customizar o retorno dessa função da seguinte forma: `np.arange(start, stop, step)`, que como tu deve ter aprendido na escola, quer dizer início, fim e passo. Por exemplo, podemos obter um array que inicia em 2 e para em 21, pulando de 2 em 2 números. 

```
np.arange(2, 21, 2)
output: array([ 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
```

Feitoria, a função **`arange()`** é bem *safe* de manusear e é muito utilizada para criar arrays com dados de teste ou até mesmo pré-popular matrizes, mas iremos falar delas mais tarde, jovem mancebo. Por hora, vamos abordar outra maneira de criar arrays, que bom, é utilizando a função **`array()`**. 

Essa função recebe um iterável como parâmetro, seja uma lista, uma tupla ou um outro array, e te joga um novo array como retorno. Uau!

<p align="center">
  <img src="https://media1.tenor.com/images/c3c09dfacd87516c3ba1cdad29aa8aaa/tenor.gif?itemid=7331473" height=200>
</p>

```
array1 = np.array([1,2,3,4,5,6])
output: array([1, 2, 3, 4, 5, 6])
```

Estes dois arrays mostrados acima, são chamados de **unidimensionais**, ou 1-D, justamente pois tem... uma dimensão :D.

<p align="center">
  <img src="https://media1.tenor.com/images/e5e91360089456411ef660428fb48270/tenor.gif?itemid=9900289" height=200>
</p>


É possível visualizar o número de formato de um array, para identificar o número de dimensões em que ele está disposto, com o atributo `shape`.

```
array1 = np.array([1,2,3,4,5,6])
array1.shape
output: (6,)
```

Perceba que o retorno é composto por apenas um número, ou seja, a quantidade de elementos dispostos no array de uma dimensão. Se retornasse dois números, saberíamos que seria de duas dimensões. Obrigado capitão.


Podemos mudar o formato de um array, ou seja, alterar o número de dimensões, com a função `reshape()`. Vamos testar aqui, pois quem sabe faz ao vivo. *O lokinho meu*.

```
# Utilizando o mesmo array do exemplo anterior
array1 = np.array([1,2,3,4,5,6])
array1.reshape(3,2)
output:	array([[1, 2], 
	      [3, 4], 
	      [5, 6]])
```

A função `reshape()`, nesse caso, recebeu dois parâmetros: o `número de linhas` e o `número de colunas`, e se configurou em formato de **matriz (3x2)**. Se tornando assim, um fuckin' vetor bimensional.

<p align="center">
  <img src="https://media1.tenor.com/images/8be72b833a199b2037ffc0d3b83c50b8/tenor.gif?itemid=3404840" height=200>
</p>

Um fato interessante é que, por mais que nós, seres humanos completamente normais e racionais, consigamos compreender e visualizar no máximo 3 dimensões do mundo real, os arrays podem estar dispostos em quantas dimensões forem necessárias, neste caso, apenas em duas.

Um outro fato curioso sobre os arrays é que, por mais que o nome NumPy remeta a números, os arrays não são exclusivos para processamento numérico. "Ué como assim jão??". É isso mesmo, os arrays podem armazenar dados de qualquer tipo, incluindo tipos variados de dados em um mesmo array (o que aliás é fortemente não recomendado). Para exemplificar, vamos criar um array contendo apenas strings:

```
np.array(['reskein', 'xesque', 'dale', 'pog'])
output: array(['reskein', 'xesque', 'dale', 'pog'], dtype='<U7')
```

Se você é um sujeito esperto e altamente pogchamp (talvez mono Aurelion Sol, Azir ou Garen <img src="https://i.kym-cdn.com/photos/images/newsfeed/000/925/494/218.png_large" height=30>), deve ter notado algo novo no nosso output: um atributo chamado ``dtype``. Bom, o NumPy precisa identificar qual, ou quais, **tipo de dado** está presente no seu array, já que "1" não é a mesma coisa que 1 e False não é a mesma coisa que "False". O NumPy, além disso, pela mesma questão de eficiência discutida anteriormente, trabalha com alguns tipos diferentes do Python (int, float, str...), sendo eles:
-   i - inteiro
-   b - booleano
-   u - inteiro "unsigned"
-   f - float
-   c - float complexo
-   m - timedelta 
-   M - valores de data
-   O - objeto
-   S - string
-   U - unicode string
-   V - parte fixa de memória de outro tipo ( void )
