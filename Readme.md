# 🔍 Port Scanner TCP/IP Assíncrono (v1)

Projeto educacional de um **Port Scanner TCP assíncrono** desenvolvido em Python, com foco no estudo de **redes de computadores**, **protocolo TCP/IP**, **concorrência** e **noções básicas de cibersegurança**.

Esta é a **primeira versão do projeto**, com implementação simples e didática.

---

## 🎯 Objetivos do Projeto

- Compreender o funcionamento do **protocolo TCP/IP**
- Entender o conceito de **portas e serviços**
- Explorar **programação assíncrona** com `asyncio`
- Aplicar controle de concorrência com **semáforos**
- Introduzir conceitos iniciais de **cibersegurança**

---

## 🧠 Tipo de Scan Implementado

- **TCP Connect Scan**
  - Realiza o **three-way handshake completo**
  - Utiliza `asyncio.open_connection`
  - Detecta portas:
    - Abertas
    - Fechadas
    - Sem resposta (timeout / filtradas)

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- Biblioteca padrão:
  - `asyncio`

> Nenhuma dependência externa é necessária.

---

## ▶️ Como Executar

1. Clone o repositório:
```bash
git clone https://github.com/victorw29/python-tcp-port-scan
```
2. Acesse o repositório:
    cd python-tcp-port-scan

3. Execute no terminal:
    python portscan.py



