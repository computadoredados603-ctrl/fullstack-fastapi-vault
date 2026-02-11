# 🛡️ BullAssets - Full Stack Vault

Sistema de gerenciamento de ativos desenvolvido com **Python (FastAPI)** e **Tailwind CSS**. Este projeto foca em design premium, responsividade e, principalmente, na implementação de normas rigorosas de **segurança de dados**.

## 🚀 Tecnologias e Agilidade
Utilizei IA para acelerar o desenvolvimento de códigos repetitivos, permitindo focar 100% na **arquitetura do sistema** e na experiência do usuário.

- **Backend:** FastAPI (Python)
- **Frontend:** HTML5 & Tailwind CSS
- **Banco de Dados:** SQLAlchemy (SQLite)

## 🔒 Implementações de Segurança (Normas de Dados)
Como parte do meu aprendizado contínuo na **Estácio**, este projeto foi blindado contra vulnerabilidades comuns:

* **Sanitização de Backend:** Implementação da biblioteca `Bleach` para limpar inputs e prevenir ataques de **XSS (Cross-Site Scripting)**.
* **Validação de Frontend:** Uso de atributos `maxlength` e `pattern` (Regex) nos formulários para garantir a integridade dos dados enviados.
* **Proteção de Arquivos:** Configuração estratégica de `.gitignore` para impedir o vazamento de bancos de dados (`.db`) e variáveis de ambiente (`.env`).
* **Gestão de Dependências:** `requirements.txt` padronizado para garantir um ambiente de execução seguro e controlado.

## 🛠️ Como rodar o projeto
1. Instale as dependências: `pip install -r requirements.txt`
2. Inicie o servidor: `uvicorn main:app --reload`