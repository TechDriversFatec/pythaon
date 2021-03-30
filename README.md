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
| Inserir exemplo de currículo e criar busca simples  | Concluído  |

#### Sprint 02

#### Sprint 03

#### Sprint 04

## Diagrama de caso de uso:
![Casos de uso](/Documentos/CasoUso1.png)
## Modelo do banco de dados:
**Vaga**
```json
{
   "vigenciaDataInicial":"01/01/2021",
   "vigenciaDataFinal":"31/12/2021",
   "urgencia":"baixa",
   "requisitos":[
      {
         "desc":"Tecnico em informatica"
      }
   ],
   "endereco":[],
   "contato":[]
}
```

**Currículo**
```json
{
  "nome":"arthur cardoso",
  "dataNasc":"25/09/00",
  "rg":"37.715.750-8",
  "formacao" : [
   {
      "desc" : "tecnico informatica",
      "instituicao": "instituicao",
      "concluido":"01/01/2021",
      "previaConclusao":"???"
    }
  ],
  "exp":[
     {
      "cargo":"Tecnico em informatica",
      "desc":"Tecnico informatica e suporte",
      "dataInicio":"01/01/2021",
      "dataFinal":""
    }
  ],
  "endereco":[],
  "contato":[]
}
```

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
