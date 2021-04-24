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
| Criar buscas de currículos por parâmetros | Em andamento |
| Criar buscas por geolocalização | Em andamento |
| Atualizar estruturas e cadastros para receber geolocalização | Em andamento |

#### Sprint 04

## Diagrama de caso de uso:
![Casos de uso](/Documentos/CasoUso1.png)
## Modelo do banco de dados:
**Vaga**
```json
{
    "VagaIdExterno":"1",
    "tituloVaga":"desc da vaga",
    "tipoContratacaoPerfilVaga":"clt",
    "tipoJornadaPerfilVaga":"liberal",
    "localEnderecoCEPPerfilVaga":"12345-600",
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

**Currículo**
```json
{
    "InscritoIdExterno":"1",
    "rgInscrito":"123.123.123-12",
    "dataNascimentoInscrito":"25/09/2000",
    "sexoInscrito":"masculino",
    "telefoneCelularInscrito":"(12)12344321",
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
## Documentação da API
<details >
<summary>
<b>🟦GET</b>  /buscarvaga_vaga/[Id da Vaga]/ 
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
<b>🟩POST</b> /insert_vaga/
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
<b>🟩POST</b> /update_vaga/
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
<b>🟥DELETE</b> /delete_vaga/[Id da Vaga]/
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
<b>🟦GET</b>  /buscaCurriculo/[Id do currículo]/
</summary>
</details>

<details>
<summary>
<b>🟩POST</b> /cadastrar_curriculo/
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
   "message": "Currículo inserida com sucesso"
}
```
</details>

<details>
<summary>
<b>🟩POST</b> /atualizar_curriculo/[Id do currículo]
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
<b>🟥DELETE</b> /deletar_curriculo/[Id do currículo]/
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
<b>🟦GET</b>  /buscaPorVaga/[Id da Vaga]/
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
