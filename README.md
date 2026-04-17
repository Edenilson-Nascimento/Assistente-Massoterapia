# 💆‍♂️ Assistente de Massoterapia com IA

Aplicação interativa desenvolvida com **Streamlit** que utiliza Inteligência Artificial para auxiliar massoterapeutas e estudantes na criação de protocolos e esclarecimento de dúvidas técnicas.

> ⚠️ Este sistema não substitui avaliação médica ou fisioterapêutica. Seu uso é educativo e de apoio profissional.

---

## 🚀 Funcionalidades

* 💬 Chat inteligente para dúvidas em massoterapia
* 📋 Geração automática de protocolos de atendimento personalizados
* 🧠 IA especializada em anatomia muscular e técnicas manuais
* 📄 Exportação de protocolos em PDF
* ⚙️ Interface simples e interativa via navegador

---

## 🛠️ Tecnologias Utilizadas

* **Python**
* **Streamlit** (interface web)
* **Groq API** (modelo de linguagem)
* **python-dotenv** (gerenciamento de variáveis de ambiente)
* **ReportLab** (geração de PDF)

---

## 🧠 Como funciona

O sistema utiliza um **prompt estruturado e validado** para garantir:

* precisão anatômica
* respostas didáticas
* organização profissional
* segurança nas recomendações

A IA segue um padrão com:

* região tratada
* músculos envolvidos
* técnicas recomendadas
* contraindicações
* cuidados pós atendimento

---

## ⚙️ Como rodar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

### 2. Acesse a pasta

```bash
cd seu-repositorio
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

> Caso não tenha o requirements.txt, instale manualmente:

```bash
pip install streamlit groq python-dotenv reportlab
```

---

### 4. Configure a variável de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
GROQ_API_KEY=sua_chave_aqui
```

---

### 5. Execute o projeto

```bash
streamlit run app.py
```

---

## 📌 Estrutura do Projeto

```
📁 projeto
 ┣ 📄 app.py
 ┣ 📄 .env
 ┣ 📄 requirements.txt
 ┗ 📄 README.md
```

---

## 🏷️ Versão

### v1.0 - Primeira versão funcional
- Assistente com IA para dúvidas em massoterapia
- Geração de protocolos personalizados
- Exportação em PDF


## 📋 Roadmap

* [ ] Histórico de atendimentos
* [ ] Login de usuários
* [ ] Cadastro de terapeutas
* [ ] Personalização da IA por perfil
* [ ] Deploy online
* [ ] Correção da formatação do pdf 

---

## 🤝 Contribuição

Contribuições são bem-vindas!

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/nova-feature`)
3. Commit (`git commit -m 'feat: nova funcionalidade'`)
4. Push (`git push origin feature/nova-feature`)
5. Abra um Pull Request

---

## 📄 Licença

Este projeto está sob a licença MIT.

---

## 👨‍💻 Autor

**Edenilson Nascimento**

* LinkedIn: https://www.linkedin.com/in/edenilson-nascimento-dev/

---

## 💡 Visão do Projeto

Este projeto faz parte de uma iniciativa de desenvolvimento na área de **HealthTech**, unindo tecnologia e bem-estar para criar soluções acessíveis e inteligentes para profissionais da saúde.

---
