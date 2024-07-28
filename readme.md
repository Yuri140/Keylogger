# Keylogger

Este é um projeto de keylogger educacional desenvolvido para fins de aprendizado em um ambiente controlado. O objetivo deste projeto é demonstrar como um keylogger pode ser implementado, destacando as técnicas básicas de captura de teclas, captura de tela, ocultação e persistência no sistema. **Este projeto deve ser usado apenas para fins educacionais em um ambiente de teste.**

## Funcionalidades

- Captura de teclas pressionadas e armazenamento em um banco de dados MySQL.
- Captura de screenshots periódicas e armazenamento no banco de dados.
- Ocultação do console de execução.
- Persistência através da criação de uma tarefa agendada no Windows.

## Requisitos

- Python 3.6 ou superior
- MySQL
- XAMPP (opcional, para fácil configuração do MySQL e phpMyAdmin)

## Instalação

1. **Clone o repositório:**

    ```sh
    git clone https://github.com/Yuri140/keylogger.git
    cd keylogger
    ```

2. **Instale as dependências:**

    ```sh
    pip install pynput mysql-connector-python pyautogui Pillow pyscreeze
    ```

3. **Configuração do Banco de Dados:**

    - Execute o banco de dados MySQL chamado `keyloggerdb`.
    - Crie um usuário com todas as permissões para este banco de dados:
    
        ```sql
        CREATE USER 'goldfire'@'localhost' IDENTIFIED BY '123456';
        GRANT ALL PRIVILEGES ON keyloggerdb.* TO 'goldfire'@'localhost';
        FLUSH PRIVILEGES;
        ```

## Uso

1. **Execute o script keylogger:**

    ```sh
    python keylogger.py
    ```

2. **O script irá:**
    - Ocultar a janela do console.
    - Criar uma tarefa agendada para persistência.
    - Capturar teclas pressionadas e armazenar no banco de dados.
    - Capturar screenshots a cada minuto e armazenar no banco de dados.

## Considerações Importantes

**Aviso Legal**: Este projeto é destinado exclusivamente para fins educacionais em um ambiente de teste controlado. A utilização de keyloggers em sistemas sem a devida autorização é ilegal e antiética. Certifique-se de ter permissão explícita para executar este software no ambiente em que pretende utilizá-lo.