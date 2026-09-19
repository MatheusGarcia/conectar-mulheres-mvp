# Conectar Mulheres — MVP 1

Aplicação web mobile-first para acesso discreto a informação e à rede de apoio para mulheres em João Pessoa/PB. O MVP usa Python + Flask, não possui login, banco de dados, analytics ou envio automático de mensagens.

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
