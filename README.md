<h1>
    <span>DESAFIO DIO - Bootcamp Python AI Backend Developer</span>
</h1>

## Objetivo
Repositório criado para concluir o desafio proposto pela  [DIO](https://www.dio.me/): **Otimizando o Sistema Bancário com Funções Python**

- Primeira Versão do Sistema Bancário:

    <td align="center">
        <a href="https://github.com/camila-vieirao/sistema-bancario-v1">
           <img align="center" alt="Sistema Bancário 1" src="https://img.shields.io/badge/Versão%201.0-E94D5F?style=for-the-badge">
        </a>
    </td>

## O que há de novo?   

O novo sistema ainda realiza as mesmas operações de antes, mas agora elas são implementadas em funções. Além disso, ele possui **duas novas funções**:

<table>
  <thead>
    <tr align="left">
      <th>Nº</th>
      <th>Função</th>
      <th>V. 1.0</th>
      <th>V. 2.0</th>
    </tr>
  </thead>
    <tr>
      <td>01</td>
      <td>Saque</td>
      <td>✅</td>
      <td>✅</td>
    </tr>
    <tr>
      <td>02</td>
      <td>Depósito</td>
      <td>✅</td>
      <td>✅</td>
    </tr>
        <tr>
      <td>03</td>
      <td>Visualização de Extrato</td>
      <td>✅</td>
      <td>✅</td>
    </tr>
    <tr>
      <td>04</td>
      <td>Criar Usuário</td>
      <td>❌</td>
      <td>✅</td>
    </tr>
      <td>05</td>
      <td>Criar Conta Corrente</td>
      <td>❌</td>
      <td>✅</td>
    </tr>
</table>


## Requisitos para o Desafio:

### 1. Função Saque   
- A função saque recebe os argumentos **apenas por nome** (*keyword only*).

### 2. Função Depósito
- A função depósito recebe argumentos **apenas por posição** (*positional only*).

### 3. Função Extrato
- A função extrato recebe os argumentos por **posição e por nome**.

### 4. Criar Usuário
- O programa armazena os usuários em uma lista.
- Um **Usuário** deve ser composto por: **nome, data de nascimento, CPF e endereço**.
- O **Endereço** é uma string com o formato: **logradouro, num - bairro - cidade/UF**.
> ⚠️ **Não é possível cadastrar dois usuários com o mesmo CPF.**

### 5. Criar Conta Corrente
- O programa armazena as contas em uma lista.
- Uma **Conta** é composta por: **agÊncia, número da conta, e usuário**.
- O número da conta é sequêncial, iniciando em 1. O número da agência é fixo: "0001".
> ⚠️ **Um usuário pode ter mais de uma conta, mas uma conta pertence a apenas um usuário.**