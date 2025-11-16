# 🚀 README: Comparador de Respostas LLM 

Este projeto é um script Python simples (`app.py`) que compara as respostas geradas por diferentes modelos de linguagem a partir de um conjunto de perguntas fornecido em um arquivo de texto.

---

## 🏗️ Pré-requisitos

Para executar este projeto, você precisa ter o **Docker** e o **Docker Compose** instalados em seu sistema.

* **Docker:** É usado para criar um ambiente isolado e consistente para a execução do script.
* **Docker Compose:** É usado para gerenciar a execução do contêiner, garantindo que todas as dependências (como as variáveis de ambiente) sejam configuradas corretamente.

---

## ⚙️ Configuração

### 1. Obter as Chaves de API

Este projeto requer chaves de API para os serviços **Gemini (Google AI)** e **Groq**.

| Serviço | Variável de Ambiente | Onde Obter a Chave |
| :--- | :--- | :--- |
| **Gemini** | `GEMINI_API_KEY` | Google AI Studio (ou Google Cloud) |
| **Groq** | `GROQ_API_KEY` | Groq Console |

### 2. Definir o Conteúdo de Entrada

Dentro do diretório raiz há um arquivo chamado perguntas.txt. Este arquivo de texto possui o system prompt para as LLMS e duas perguntas exemplos a partir do modelo especificado. Você pode editar este arquivo para adicionar suas próprias perguntas ou modificar o prompt conforme necessário.

### 3. Configurar o Docker Compose

O arquivo `docker-compose.yml` será usado para construir a imagem, montar o volume do código e injetar as chaves de API.

**Altere o arquivo `docker-compose.yml` para substituir os valores de exemplo (`COLOQUE_SUA_CHAVE_AQUI`) pelas suas chaves de API reais:**

```yaml
services:
  app:
    environment:
      # SUBSTITUA pelo seu valor real da chave Gemini
      - GEMINI_API_KEY=COLOQUE_SUA_CHAVE_GEMINI_AQUI
      # SUBSTITUA pelo seu valor real da chave Groq
      - GROQ_API_KEY=COLOQUE_SUA_CHAVE_GROQ_AQUI
    build: .
    working_dir: /app
    volumes:
      - .:/app
    command: python app.py
```

## Usando a aplicação

### 1. Construir o conteiner Docker
No terminal, dentro do diretório raiz do projeto, execute o seguinte comando para construir a imagem Docker:

```bash
docker-compose build
```
### 2. Executar o contêiner Docker
Após a construção da imagem, execute o contêiner com o seguinte comando:

```bash
docker-compose up
```
### 3. Visualizar os resultados
O script `app.py` lerá as perguntas do arquivo `perguntas.txt`, enviará cada pergunta para os modelos, e criará dois arquivos .json com todas as respostas geradas por cada modelo.

Os arquivos de saída serão:
- `respostas_gemini.json`: Contém as respostas geradas pelo modelo Gemini.
```json
[
    {
        "id": 1,
        "pergunta": "Como está o contexto de segurança cibernética na Bahia?",
        "resposta": "O contexto de segurança cibernética na Bahia reflete e, em muitos aspectos, amplifica os desafios e tendências observados no cenário nacional brasileiro. Com a crescente digitalização de serviços públicos e privados na região, a superfície de ataque para criminosos cibernéticos tem se expandido. Os principais desafios incluem a proliferação de ataques como phishing, golpes digitais (especialmente envolvendo o PIX), ransomware e vazamentos de dados, que afetam tanto indivíduos quanto organizações. Há uma necessidade contínua de aumentar a conscientização sobre os riscos cibernéticos entre a população e de capacitar profissionais, pois a escassez de especialistas é um fator limitante. A implementação da Lei Geral de Proteção de Dados (LGPD) tem impulsionado a busca por conformidade, mas pequenas e médias empresas e órgãos públicos frequentemente enfrentam dificuldades devido à limitação de recursos. Em suma, a Bahia está em um processo de adaptação à era digital, onde a segurança cibernética é um pilar essencial para proteger dados, manter a confiança e garantir a resiliência de sua infraestrutura digital."
    },
    {
        "id": 2,
        "pergunta": "Que tipos de senhas são consideradas fortes na Bahia?",
        "resposta": "A definição de senhas fortes é universal e não possui variações geográficas específicas para a Bahia. Uma senha é considerada forte quando é difícil de adivinhar ou quebrar por meio de ataques de força bruta ou dicionário. As características essenciais de uma senha forte incluem:\n-   **Comprimento:** Recomenda-se um mínimo de 12 a 16 caracteres, mas quanto mais longa, melhor (passphrases são ideais).\n-   **Diversidade de caracteres:** Deve ser uma combinação de letras maiúsculas e minúsculas, números e símbolos.\n-   **Aleatoriedade:** Não deve conter informações pessoais óbvias, palavras comuns de dicionário (mesmo com substituições simples como 'S3nh4') ou padrões sequenciais/de teclado (ex: '123456', 'qwerty').\n-   **Exclusividade:** Cada conta deve ter uma senha única para evitar o risco de comprometimento em cascata.\n-   **Uso de Gerenciadores de Senhas:** Ferramentas que geram e armazenam senhas complexas de forma segura são altamente recomendadas.\n-   **Autenticação de Dois Fatores (2FA/MFA):** Embora não seja uma característica da senha em si, a habilitação do 2FA/MFA adiciona uma camada de segurança vital, mesmo que a senha seja descoberta."
    }
]
``` 

- `respostas_groq.json`: Contém as respostas geradas pelo modelo Groq.

```json
[
    {
        "id": 1,
        "pergunta": "Como está o contexto de segurança cibernética na Bahia?",
        "resposta": "O contexto de segurança cibernética na Bahia enfrenta desafios semelhantes ao resto do Brasil, com uma variedade de ameaças cibernéticas, incluindo phishing, ransomware, golpes digitais e vazamentos de dados. A implementação da Lei Geral de Proteção de Dados (LGPD) tem impulsinado a conscientização sobre a importância da segurança de dados, mas ainda há um longo caminho a percorrer em termos de adequação e implementação de práticas de segurança robustas por parte das empresas e órgãos públicos. A região também luta contra a falta de investimento, conhecimento técnico e recursos humanos qualificados em cibersegurança, o que coloca os residentes e as organizações em um estado de vulnerabilidade."
    },
    {
        "id": 2,
        "pergunta": "Que tipos de senhas são consideradas fortes na Bahia?",
        "resposta": "Senhas fortes na Bahia, assim como em qualquer outro lugar, são aquelas que são complexas, únicas e difíceis de serem quebradas por meio de ataques de força bruta ou dicionário. Características de senhas fortes incluem: ter uma combinação de letras maiúsculas e minúsculas, números, símbolos e ter pelo menos 12 caracteres de comprimento. Além disso, elas não devem serbaseadas em informações pessoais, palavras comuns do dicionário ou padrões óbvios. É recomendável usar geradores de senhas para criar senhas aleatórias e uniqúas para cada conta, e armazená-las com segurança em um gerenciador de senhas."
    }
]
```
