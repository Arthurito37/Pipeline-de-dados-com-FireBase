# Nome do Projeto

Uma breve descrição do que o projeto faz e seu objetivo.

## Tabela de Conteúdos

- [Resumindo](#resumindo)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Instalação](#instalação)
- [Uso](#uso)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Resumindo

Basicamente, o que estamos fazendo é:

1. **Entrando no Firebase com nossa chave secreta**: Usamos um arquivo de credenciais para autenticar nossa aplicação no Firebase.
2. **Pegando todos os arquivos do nosso depósito (Storage)**: Listamos e baixamos todos os arquivos armazenados no Firebase Storage.
3. **Lendo cada arquivo, linha por linha**: Processamos o conteúdo de cada arquivo, dividindo em linhas para melhor manipulação.
4. **Transformando cada linha em um formato legal**: Estruturamos os dados de cada linha em um formato organizado e compreensível.
5. **Guardando essa informação no nosso armário gigante (Firestore)**: Armazenamos os dados processados no Firestore, que funciona como um banco de dados para acessar as informações facilmente no futuro.

É como se estivéssemos pegando um monte de papéis soltos, organizando-os de um jeito legal e guardando tudo em pastas bem arrumadas. Assim, fica muito mais fácil de achar as informações depois!

## Tecnologias Utilizadas

- Python
- Firebase Admin SDK
- Pandas
