# Sistema de Gestão de Denúncias - Projeto Integrador

## Descrição

Este projeto é uma aplicação web desenvolvida para o registro e acompanhamento de denúncias, com o objetivo de proporcionar uma plataforma simples e eficiente para a gestão de problemas reportados por usuários. Através desta ferramenta, administradores podem registrar, consultar, atualizar o status das denúncias e gerar relatórios de acompanhamento, facilitando a resposta e a resolução dos casos.

O projeto foi desenvolvido como parte do **Projeto Integrador** do **Centro Universitário CESMAC**, com foco na aplicação de tecnologias de desenvolvimento web para a criação de soluções práticas que atendem a uma necessidade real de gestão de denúncias em diversas instituições, como organizações públicas e privadas.

### Autores:
- **Vitória Freire**
- **Luana Maria Leandro Rodrigues dos Santos**

## Objetivo

O principal objetivo deste projeto é criar uma plataforma para o gerenciamento de denúncias. Através da aplicação, será possível realizar o registro de denúncias, consultar registros existentes e atualizar o status de cada denúncia (de "Pendente" para "Concluída"), tudo em uma interface simples e funcional. A plataforma foi construída utilizando o framework Django, e oferece uma interface administrativa que facilita a gestão das denúncias de maneira eficiente e organizada.

## Justificativa

A necessidade de ferramentas digitais para facilitar a gestão de denúncias tem crescido em diferentes setores, como governo, empresas e organizações não governamentais. Tais plataformas permitem um acompanhamento mais transparente e eficiente dos problemas reportados. Este projeto se justifica pela demanda de uma solução tecnológica que possa melhorar a organização e gestão dessas informações, tornando o processo de acompanhamento mais ágil e seguro.

A criação de um sistema digital para gerenciar denúncias contribui para a otimização de processos administrativos e garante maior transparência e confiabilidade nas ações de resposta às demandas da sociedade ou dos colaboradores.

## Tecnologias Utilizadas

- **Django**: Framework web baseado em Python, utilizado para o desenvolvimento do backend da aplicação.
- **SQLite**: Banco de dados relacional utilizado para armazenar os dados de denúncias.
- **HTML/CSS**: Utilizados para a construção da interface do usuário (frontend), oferecendo uma experiência simples e acessível.
- **Python**: Linguagem de programação utilizada para o desenvolvimento da lógica de backend.

## Metodologia

O desenvolvimento deste projeto seguiu uma abordagem **ágil**, com o ciclo de desenvolvimento dividido nas seguintes etapas:

1. **Planejamento e Levantamento de Requisitos**: Definição das funcionalidades principais do sistema, incluindo registro de denúncias e gestão do status.
2. **Desenvolvimento Backend**: Implementação da lógica de gerenciamento de denúncias utilizando Django e modelagem de dados no banco SQLite.
3. **Desenvolvimento Frontend**: Criação das páginas HTML para a visualização das denúncias e do painel administrativo.
4. **Testes e Validação**: Realização de testes unitários e de usabilidade para garantir a eficácia do sistema.
5. **Documentação**: Elaboração de documentação para descrever as funcionalidades do sistema e o processo de configuração.

## Como Rodar o Projeto

### Pré-requisitos

1. Instale o Python (versão 3.8 ou superior) em seu sistema.
2. Instale o Django:

```bash
pip install django
```

3. Clone o repositório para sua máquina local:

```bash
git clone https://github.com/seu-usuario/sistema-de-denuncias.git
```

### Passos para Executar

1. Navegue até o diretório do projeto:

```bash
cd sistema-de-denuncias
```

2. Execute as migrações para criar o banco de dados:

```bash
python manage.py migrate
```

3. Crie um superusuário para acessar a interface administrativa:

```bash
python manage.py createsuperuser
```

4. Inicie o servidor de desenvolvimento:

```bash
python manage.py runserver
```

5. Acesse o projeto através do navegador: [http://127.0.0.1:8000](http://127.0.0.1:8000).

6. Acesse a área administrativa em [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) com as credenciais do superusuário que você criou.


## Resultados Esperados

O sistema foi desenvolvido com sucesso, permitindo aos administradores registrar denúncias, atualizar o status das mesmas e realizar pesquisas por diferentes critérios, como nome, e-mail, status e data de criação. A plataforma permite uma gestão mais eficiente das denúncias e facilita a comunicação entre usuários e administradores.

## Conclusão

Este projeto foi desenvolvido como parte do **Projeto Integrador** e visa demonstrar a aplicação de tecnologias web na resolução de problemas reais relacionados à gestão de denúncias. A solução oferece uma interface simples e funcional, permitindo a fácil gestão das denúncias de forma ágil e segura.

## Bibliografia

- Django Software Foundation. (2023). *Django Documentation*. Disponível em: https://www.djangoproject.com/
- Martins, R. A. (2021). *Gestão de sistemas de denúncia: Desafios e soluções tecnológicas*. Editora Acadêmica.
- Silva, F. J. (2019). *Desenvolvimento de Aplicações Web com Django: Uma abordagem prática*. Editora Tecnologia.
- Oliveira, L. G. (2020). *Gestão e segurança em sistemas web: Teorias e práticas*. Editora Acadêmica.

---
