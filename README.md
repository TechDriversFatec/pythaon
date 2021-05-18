# <h1>Projeto Integrador 4º Semestre BD - Grupo Pythaon</h1>

GitLab para desenvolvimento do Projeto Integrador do 4º Semestre - Banco de dados FATEC SJC

## Quem somos?
Olá! Muito prazer! 
Nós somos o grupo Pythaon, um time de alunos do 4° semestre do curso de Banco de Dados da FATEC de São José dos Campos. Esse grupo tem como objetivo desenvolver um projeto (PI) para solucionar um problema proposto por um cliente parceiro da instituição.

## O problema
O setor de RH precisa de uma solução parametrizável que combine diversos critérios, para
busca de candidatos em diferentes vagas com diferentes recrutadores numa proposta de
processo eficiente para contratação e evasão de funcionários, reduzindo custos e
aumentando a satisfação com alocações mais adequadas.

## Proposta do projeto
Nossa proposta é desenvolver um sistema para a otimização e que facilite o processo de contratação de novos colaboradores , respeitando os requisitos, visando a rapidez e agilidade no processo. Para que esses objetivos sejam atingidos, utilizaremos uma um SGBD orientado a documentos (MongoDB), visando que as estruturas de currículos e vagas são maleáveis e se aproveitam bem da estrutura de documento usada, além de questões de desempenho e funcionalidades que podem ser aproveitadas. 

## Requisitos Funcionais

| Requisitos funcionais             |  Código |              Descrição                                                                                                                                     |Prioridade|
| ----------------------------------|---------| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|
|Interface              |RF01     |Criar interface de gerenciamento de currículos e vagas|    1     |
|Armazenagem                  |RF02     |Armazenar os currículos e vagas em um banco de dados orientado a documentos|    2     |
|Sistema de busca         |RF03     |Criar mecanismos que possibilitem buscas por currículos baseadas em vagas |    3     |   
|Filtros configurais                     |RF04     |Permitir que o usuário escolha quais filtros serão aplicados na busca e seu peso|    4     | 
|Otimização         |RF03     |Otimizar as buscas e a organização dos dados |    5     |   
## Requisitos Não Funcionais

| Requisitos funcionais             |  Código |                                                                                                                                    
| ----------------------------------|---------|
|Arquitetura do BD             |RF01     |
|Desempenho                |RF02     |
|Segurança (Safety)         |RF03     |
|Documentação específica                     |RF04     | 

## Backlog do Projeto:

#### Sprint 01
| Requisito           | Status |  
| ----------------------------------|---------|
| Definir estrutura do projeto  | Concluído  |
| Definir funcionalidades iniciais  | Concluído  |
| Definir estrutura exemplo do documento de candidato  | Concluído  |
| Implementação da conexão com MongoDB  | Concluído  |
| Inserir exemplo de currículo e criar busca simples  | Concluído |

#### Sprint 02
| Requisito           | Status |  
| ----------------------------------|---------|
| Definir estrutura para currículo | Concluído |
| Definir estrutura para vaga | Concluído |
| Criar interface crud de candidatos | Concluído |
| Criar interface crud de vagas | Concluído |
| Criar método de busca de currículos por vaga | Concluído |
| Iniciar a documentação de uso das APIs do projeto | Concluído |


#### Sprint 03
| Requisito           | Status |  
| ----------------------------------|---------|
| Criar buscas de currículos por parâmetros | Concluído |
| Criar buscas por geolocalização | Concluído |
| Atualizar estruturas e cadastros para receber geolocalização | Concluído |
| Pesquisar por currículos compatíveis quando | Concluído |

#### Sprint 04

## Diagrama de caso de uso:
![Casos de uso](/Documentos/CasoUso1.png)
## Modelo do banco de dados:
**Vaga**
```json
{
    "VagaIdExterno": "11",
    "tituloVaga": "Observer Inscrito Seleionado",
    "tipoContratacaoPerfilVaga": "clt",
    "tipoJornadaPerfilVaga": "liberal",
    "localEnderecoCEPPerfilVaga": "12231810",
    "localEnderecoPerfilVaga": "rua, bairro",
    "localEnderecoNumeroPerfilVaga": "1234",
    "faixaEtariaInicioPerfilVaga": "21",
    "faixaEtariaFimPerfilVaga": "35",
    "tempoExperienciaPerfilVaga": "2 anos",
    "faixaSalarioInicioPerfilVaga": "2500.00",
    "dataInicioDivulgacaoPerfilVaga": "01/1/2021",
    "datafinaldivulgacaoPerfilVaga": "31/01/2021",
    "competencia": [{
        "descricao": "developer"
    }],
    "PalavraChave": [{
        "DescricaoPalavraChave": "Chave"
    }],
    "IncritoIdSelecionado": [],
    "ValeTransporte": "1",
    "coordenadas": {
        "type": "Point",
        "coordinates": [-23.2406, -45.9003]
    }
}
```

**Currículo**
```json
{
    "InscritoIdExterno": "1",
    "rgInscrito": "123.123.123-12",
    "dataNascimentoInscrito": "25/09/2000",
    "sexoInscrito": "masculino",
    "telefoneCelularInscrito": "(12)9816719999",
    "jornadaDesejadaInscrito": "padrão",
    "tipoContratoDesejadoInscrito": "clt",
    "EmailInscrito": "email@email.com",
    "perfilProfissionalTituloInscrito": "Security coordenator",
    "perfilProfissionalDescricaoInscrito": "pleno com conhecimento em desenvolvimento full stack com node, dotnet, angular e react",
    "nomeCompletoInscrito": "arthur c",
    "enderecoCEPInscrito": "12231810",
    "enderecoLocalizacaoInscrito": "rua, bairro",
    "complementoInscrito": "",
    "experienciaProfissional": [{
        "descricao": "Desenvolvimento com front e back end",
        "duracaoTempoExperiencia": "2 anos"
    }],
    "competencia": [{
        "descricao": "poliglota"
    }],
    "formacao": [{
        "curso": "banco de dados",
        "Dataformacao": "22/06/2020",
        "intituicao": "fatec"
    }],
    "coordenadas": {
        "type": "Point",
        "coordinates": [-23.2406, -45.8994]
    }
}
```
## Documentação da API
<details >
<summary>
<b>🟦GET</b>  /buscar_vaga/[Id da Vaga]/ 
</summary>

Busca uma vaga por id.
<p>Response 200:</p>

``` json
{
    "VagaIdExterno":"1",
    "tituloVaga":"desc da vaga",
    "tipoContratacaoPerfilVaga":"clt",
    "tipoJornadaPerfilVaga":"liberal",
    "localEnderecoCEPPerfilVaga":"12345-111",
    "localEnderecoPerfilVaga":"rua, bairro",
    "localEnderecoNumeroPerfilVaga":"1234",
    "faixaEtariaInicioPerfilVaga":"21",
    "faixaEtariaFimPerfilVaga":"35",
    "tempoExperienciaPerfilVaga":"2 anos",
    "faixaSalarioInicioPerfilVaga":"2500.00",
    "dataInicioDivulgacaoPerfilVaga":"01/1/2021",
    "datafinaldivulgacaoPerfilVaga":"31/01/2021",
    "competencia": [
        {
         "descricao": "poliglota",
        }
    ],
     "PalavraChave" :[
         {
            "DescricaoPalavraChave":"Chave",
         }
    ],
}
```
</details>

<details>
<summary>
<b>🟩POST</b> /inserir_vaga
</summary>
Insere uma vaga.
<p>Exemplo de parâmetro:</p>

``` json
{
    "VagaIdExterno":"1",
    "tituloVaga":"desc da vaga",
    "tipoContratacaoPerfilVaga":"clt",
    "tipoJornadaPerfilVaga":"liberal",
    "localEnderecoCEPPerfilVaga":"12345-111",
    "localEnderecoPerfilVaga":"rua, bairro",
    "localEnderecoNumeroPerfilVaga":"1234",
    "faixaEtariaInicioPerfilVaga":"21",
    "faixaEtariaFimPerfilVaga":"35",
    "tempoExperienciaPerfilVaga":"2 anos",
    "faixaSalarioInicioPerfilVaga":"2500.00",
    "dataInicioDivulgacaoPerfilVaga":"01/1/2021",
    "datafinaldivulgacaoPerfilVaga":"31/01/2021",
    "competencia": [
        {
         "descricao": "poliglota",
        }
    ],
     "PalavraChave" :[
         {
            "DescricaoPalavraChave":"Chave",
         }
    ],
}
```
<p>Response 200:</p>

``` json
{
   "message": "Vaga inserida com sucesso"
}
```
</details>

<details>
<summary>
<b>🟧PUT</b> /atualizar_vaga/[Id da Vaga]/ 
</summary>
Atualiza uma vaga já existente.
<p>Exemplo de parâmetro:</p>

``` json
{
    "VagaIdExterno":"1",
    "tituloVaga":"desc da vaga",
    "tipoContratacaoPerfilVaga":"clt",
    "tipoJornadaPerfilVaga":"liberal",
    "localEnderecoCEPPerfilVaga":"12345-123",
    "localEnderecoPerfilVaga":"rua, bairro",
    "localEnderecoNumeroPerfilVaga":"1234",
    "faixaEtariaInicioPerfilVaga":"21",
    "faixaEtariaFimPerfilVaga":"31",
    "tempoExperienciaPerfilVaga":"1 anos",
    "faixaSalarioInicioPerfilVaga":"2300.00",
    "dataInicioDivulgacaoPerfilVaga":"01/1/2021",
    "datafinaldivulgacaoPerfilVaga":"31/01/2021",
    "competencia": [
        {
         "descricao": "poliglota",
        }
    ],
     "PalavraChave" :[
         {
            "DescricaoPalavraChave":"Chave",
         }
    ],
}
```

<p>Response 200:</p>

``` json
{
   "message": "Vaga atualizada com sucesso"
}
```
</details>

<details>
<summary>
<b>🟥DELETE</b> /excluir_vaga/[Id da Vaga]
</summary>
Exclui a vaga baseada no parâmetro, caso encontrada.
<p>Response 200:</p>

``` json
{
   "message": "Vaga excluída com sucesso"
}
```
</details>

<details>
<summary>
<b>🟦GET</b> /buscar_curriculo/[Id do currículo]
</summary>

<p>Response 200:</p>

``` json
{
    "InscritoIdExterno":"1",
    "rgInscrito":"123.123.123-12",
    "dataNascimentoInscrito":"25/09/2000",
    "sexoInscrito":"masculino",
    "telefoneCelularInscrito":"(12)91231235",
    "jornadaDesejadaInscrito":"padrão",
    "tipoContratoDesejadoInscrito":"clt",
    "EmailInscrito":"email@email.com",
    "perfilProfissionalTituloInscrito":"full stack developer",
    "perfilProfissionalDescricaoInscrito":"pleno com conhecimento em desenvolvimento full stack com node, dotnet, angular e react",
    "nomeCompletoInscrito":"arthur c",
    "enderecoCEPInscrito":"12345-608",
    "enderecoLocalizacaoInscrito":"rua, bairro",
    "complementoInscrito":"",
    "enderecoLocalizacaoLatitudeInscrito":"",
    "enderecoLocalizacaoLongitudeInscrito":"",
    "experienciaProfissional": [
        {
         "descricao": "Desenvolvimento com front e back end",
         "duracaoTempoExperiencia":"2 anos",
         }
      ],
      "competencia": [
        {
         "descricao": "poliglota",
        }
      ],
    "formacao": [
        {
            "curso":"banco de dados",
            "Dataformacao":"22/06/2020",
            "intituicao":"fatec"
        }
      ],
}
```
</details>

<details>
<summary>
<b>🟩POST</b> /inserir_curriculo
</summary>
Cadastra um currículo.
<p>Exemplo de parâmetro:</p>

``` json
{
    "InscritoIdExterno":"1",
    "rgInscrito":"123.123.123-12",
    "dataNascimentoInscrito":"25/09/2000",
    "sexoInscrito":"masculino",
    "telefoneCelularInscrito":"(12)981612345",
    "jornadaDesejadaInscrito":"padrão",
    "tipoContratoDesejadoInscrito":"clt",
    "EmailInscrito":"email@email.com",
    "perfilProfissionalTituloInscrito":"full stack developer",
    "perfilProfissionalDescricaoInscrito":"pleno com conhecimento em desenvolvimento full stack com node, dotnet, angular e react",
    "nomeCompletoInscrito":"arthur c",
    "enderecoCEPInscrito":"12345-608",
    "enderecoLocalizacaoInscrito":"rua, bairro",
    "complementoInscrito":"",
    "enderecoLocalizacaoLatitudeInscrito":"",
    "enderecoLocalizacaoLongitudeInscrito":"",

    "experienciaProfissional": [
        {
         "descricao": "Desenvolvimento com front e back end",
         "duracaoTempoExperiencia":"2 anos",
         }
      ],

      "competencia": [
        {
         "descricao": "poliglota",
        }
      ],

    "formacao": [
        {
            "curso":"banco de dados",
            "Dataformacao":"22/06/2020",
            "intituicao":"fatec"
        }
      ],
}
```
<p>Response 200:</p>

``` json
{
   "message": "Currículo inserido com sucesso"
}
```
</details>

<details>
<summary>
<b>🟧PUT</b> /atualizar_curriculo/[Id do currículo]
</summary>
Atualiza um currículo.
<p>Exemplo de parâmetro:</p>

``` json
{
    "InscritoIdExterno":"1",
    "rgInscrito":"123.123.123-12",
    "dataNascimentoInscrito":"25/09/2000",
    "sexoInscrito":"masculino",
    "telefoneCelularInscrito":"(12)981612345",
    "jornadaDesejadaInscrito":"padrão",
    "tipoContratoDesejadoInscrito":"clt",
    "EmailInscrito":"email@email.com",
    "perfilProfissionalTituloInscrito":"full stack developer",
    "perfilProfissionalDescricaoInscrito":"pleno com conhecimento em desenvolvimento full stack com node, dotnet, angular e react",
    "nomeCompletoInscrito":"arthur c",
    "enderecoCEPInscrito":"12345-608",
    "enderecoLocalizacaoInscrito":"rua, bairro",
    "complementoInscrito":"",
    "enderecoLocalizacaoLatitudeInscrito":"",
    "enderecoLocalizacaoLongitudeInscrito":"",

    "experienciaProfissional": [
        {
         "descricao": "Desenvolvimento com front e back end",
         "duracaoTempoExperiencia":"1 anos",
         }
      ],

      "competencia": [
        {
         "descricao": "poliglota",
        }
      ],

    "formacao": [
        {
            "curso":"banco de dados",
            "Dataformacao":"22/06/2020",
            "intituicao":"fatec"
        }
      ],
}
```
<p>Response 200:</p>

``` json
{
   "message": "Currículo atualizado com sucesso"
}
```
</details>

<details>
<summary>
<b>🟥DELETE</b> /excluir_curriculo/[Id do currículo]
</summary>
Exclui o currículo baseado no parâmetro, caso encontrado.
<p>Response 200:</p>

``` json
{
   "message": "Currículo Excluído com sucesso"
}
```
</details>

<details>
<summary>
<b>🟦GET</b> /buscaPorVaga/[Id da Vaga]
</summary>
Realiza uma busca por currículo baseada na vaga enviada por parâmetro e retorna os ids dos candidatos.
<p>Response 200:</p>

``` json
{
    "candidatos": [
        "123","433","54","1123"
    ],
    "message": ""
}
```
</details>

<details>
<summary>
<b>🟦GET</b> /buscaFiltrada
</summary>
<p>Recebe um array de parâmetros dinâmicos e executa uma busca no banco de dados.<br>
A busca pode receber parâmetros de três tipos: Texto, data e localização.</p>

**Texto:**
- "tipo"  : Tipo de busca a ser realizada.
- "chave" : campo em que será realizada a busca. (String)
- "valor" : Campo que contém o conteúdo a ser buscado. Pode ser uma String ou um Array de String.(String|Array<String>)

**Localização:**
- "tipo"    : Tipo de busca a ser realizada.
- "chave"   : campo em que será realizada a busca. (String)
- "valor"   : Campo que contém as coordenadas do ponto central ao qual a busca será realizada.(Array<Float>)
- "mindist" : Campo que contém a distância mínima necessária dos inscritos para o ponto central para entrar nas condições da busca.
- "maxdist" : Campo que contém a distância máxima dos inscritos para o ponto central para entrar nas condições da busca.

**Data:**
- "tipo" : Tipo de busca a ser realizada.
- "chave": campo em que será realizada a busca. (String)
- "operador": Campo que contém o parâmetro de data.(String)

\*Os operadores são funções para comparar determinado parâmetro. Os operadores aceitos na api são:
- eq  : Encontra valores que são iguais ao valor especificado 
- ne  : Encontra valores que são diferentes ao valor especificado
- gt  : Encontra valores que são maiores ao valor especificado
- gte : Encontra valores que são maiores ou iguais ao valor especificado
- lt  : Encontra valores que são menores ao valor especificado
- lte : Encontra valores que são menores ou iguais ao valor especificado

<p>Exemplo de parâmetros de busca:</p>

``` json
[
 {
  "chave" : "rgInscrito",
  "valor" : "123",
  "tipo"  : "texto"
 },
 {
  "chave" : "formacao.curso",
  "valor" : ["banco", "Suporte"],
  "tipo"  : "texto"
 },
 {
  "tipo"  : "distancia",
  "chave" : "distancia",
  "valor" : [-23.2322,-45.9000],
  "mindist" : 0,
  "maxdist" : 2500
 },
 {
  "tipo"  : "data",	
  "chave" : "dataNascimentoInscrito",
  "gte"   : "2013-09-0100:00:00"
 }
]
```
</details>

## Tecnologias Utilizadas:
* Python/Django
* MongoDB

# INTEGRANTES

 * GABRIEL DE QUEIROZ CORDEIRO **| Product Owner |**
 * SABRINA RAFAELA CALADO MARIANO **| Dev Team |**
 * GUSTAVO RIBEIRO DOS SANTOS **| Master |**
 * ARTHUR CARDOSO RINALDI DA SILVA **| Dev Team |**
 * PERILO CARVALHO DE OLIVEIRA JUNIOR **| Dev Team |**
 * VINICIUS FERNANDES DE LIMA **| Dev Team |**
