from ExtratorArgumentosUrl import ExtratorArgumentoUrl

url = 'http://www.byte.com.br/cambio?moedaoRigem=moedadestino&moedadestino=dolar&valor=1500'

argumento = ExtratorArgumentoUrl(url)

# Retorna a string do OBJETO (argumento)
print(argumento.get_url)

# Constroi duas variáveis do OBJETO (argumento),
# as quais receberão os nomes das moedas de origem e destino:
# v1 > moeda_origem = real  e  v2 > moeda_destino = dolar
moeda_origem, moeda_destino = argumento.Extrai_argumentos_len()
print(f'MOEDAS: moeda_origem = {moeda_origem}, moeda_destino = {moeda_destino}')

# Constroi uma variável do OBJETO (argumento), a qual receberá o valor da operação:
# v > valor = 1500
valor = argumento.Extrai_valor()
print(f'Valor da operação: R${valor}')

# Testa se a url tem um valor válido, verificando se a entrada é diferente de None ou vazio "",
# e também testa se a url tem string inicial == 'http://www.byte.com.br/'
# Retorna valor boleano: True/False
teste_url = argumento.Url_valida(url)
print(f'Teste de validação da url: {teste_url}')

# Retorna a string do OBJETO (argumento) e dessa vez será diferente,
# uma vez que a função .Extrai_argumentos_len() usada previamente corrigiu o erro na variável inicial (url)
print(argumento.get_url)

# Imprime o tamanho do meu OBJETO (url)
# É necessário criar a def __len__ para implementar o método len()
print(f'Tamanho da url: {len(argumento)} caracteres')

# Imprime a 'representação string' do meu OBJETO (url)
# É necessário criar a def __str__ para implementar este print()
# Sem implementação, o retorno será: <ExtratorArgumentosUrl.ExtratorArgumentoUrl object at 0x01021FB8>
print(argumento)

url2 = 'http://www.byte.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=1500'

argumento2 = ExtratorArgumentoUrl(url2)

# Imprime a comparação entre os OBJETOs (argumento e argumento2), para saber se são iguais
# É necessário criar a def __eq__ para implementar este print()
# Sem implementação, o retorno será: False => está comparando locais na memoria (id's) ocupados pelos OBJETOs

print(f"As url's são iguais? {argumento == argumento2}")
