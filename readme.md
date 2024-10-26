# Projeto de Gerenciamento de Pedidos

Este projeto é um sistema de gerenciamento de pedidos que permite a criação e gerenciamento de clientes, pedidos e produtos. Ele utiliza Pydantic para validação de dados e pytest para testes automatizados.

## Estrutura do Projeto

src/
├── domains/
│   ├── base.py
│   ├── customer.py
│   ├── order.py
│   └── product.py
├── factories/
│   └── customer_factory.py
├── services/
│   ├── customer_service.py
│   └── exceptions/
│       └── customer_exceptions.py
└── datalayer/
    ├── interfaces/
    └── repositories/


## Dependências

- Python 3.8 ou superior
- Pydantic
- pytest

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu_usuario/seu_repositorio.git
   cd seu_repositorio
   ```

2. Crie um ambiente virtual e ative-o:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Linux/Mac
   venv\Scripts\activate  # Para Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

Para executar os testes, utilize o seguinte comando:

```bash
pytest
```

Os testes estão localizados nas pastas `tests/domains/` e `tests/services/`.

## Funcionalidades

- **Cadastro de Clientes**: Permite o registro de novos clientes com validação de e-mail.
- **Gerenciamento de Pedidos**: Criação e gerenciamento de pedidos, incluindo status e itens.
- **Cadastro de Produtos**: Permite a adição de produtos ao sistema.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir um issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
