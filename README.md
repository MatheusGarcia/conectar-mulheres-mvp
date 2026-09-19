# Conectar Mulheres — MVP 1

Aplicação web mobile-first para acesso discreto a informação e à rede de apoio para mulheres em João Pessoa/PB. O MVP usa Python + Flask, não possui login, banco de dados, analytics ou envio automático de mensagens.

**Aplicação publicada:** [conectar-mulheres-mvp.onrender.com](https://conectar-mulheres-mvp.onrender.com)

## Mockups do MVP

| Abertura discreta | Página inicial |
| --- | --- |
| <img src="docs/mockups/01-abertura.png" width="260" alt="Mockup da abertura discreta"> | <img src="docs/mockups/02-inicio.png" width="260" alt="Mockup da página inicial"> |
| **Ajuda imediata** | **Rede de apoio** |
| <img src="docs/mockups/03-ajuda-imediata.png" width="260" alt="Mockup da ajuda imediata"> | <img src="docs/mockups/04-rede-de-apoio.png" width="260" alt="Mockup da rede de apoio"> |
| **Detalhes do serviço** | **Artigos** |
| <img src="docs/mockups/05-detalhes-servico.png" width="260" alt="Mockup dos detalhes do serviço"> | <img src="docs/mockups/06-artigos.png" width="260" alt="Mockup da lista de artigos"> |
| **Leitura do artigo** | **Contato de confiança** |
| <img src="docs/mockups/07-leitura-artigo.png" width="260" alt="Mockup da leitura de artigo"> | <img src="docs/mockups/08-contato-confianca.png" width="260" alt="Mockup do contato de confiança"> |

O quadro completo e editável está em [`deliverables/conectar-mulheres-mockups-v1.svg`](deliverables/conectar-mulheres-mockups-v1.svg).

## Executar localmente

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
flask --app app run --debug
```

Acesse `http://127.0.0.1:5000`.

## Testes

```bash
pytest
```

## Publicar no Render

1. Envie o projeto para um repositório GitHub.
2. No Render, escolha **New > Blueprint** e conecte o repositório.
3. O arquivo `render.yaml` configura a instalação, inicialização e verificação de saúde.

## Limites desta versão

- A posição do usuário não é solicitada nem armazenada.
- O mapa é ilustrativo; rotas abrem o OpenStreetMap em outra aba.
- O contato de confiança é processado apenas no navegador e aberto no WhatsApp para revisão.
- Telefones e horários de serviços devem ser validados com as fontes oficiais antes da publicação pública.
