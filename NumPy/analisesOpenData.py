import pandas as pd
from scipy import stats

#1ª Análise
print("1ª Análise\n")
# Read data from CSV file

data = pd.read_csv('vacinados-2022.csv', sep=';',
                   on_bad_lines='skip', low_memory=False)

data.dropna(subset=['idade'], inplace=True)

#Após analizar as colunas, decidi por encontrar as idades das pessoas Parda e Preta,
#tomando como hipotese nula, que as idades serão iguais baseado na raça/cor da pessoa.
#Determinei os Samples baseando-se no código disponibilizado pelo professor no github.
sample1 = data[data['raca_cor'] == 'PARDA']['idade']
sample2 = data[data['raca_cor'] == 'PRETA']['idade']

#Tratamento de erro humanos dos dados coletados
sample1 = pd.to_numeric(sample1, errors='coerce')
sample2 = pd.to_numeric(sample2, errors='coerce')

#cálculo da média para comparar com o T_Teste
mediaDose1 = sample1.mean()
mediaDose2 = sample2.mean()

# exibir o resultado
print(mediaDose1)
print(mediaDose2)

# # Perform t-test
t_stat, p_value = stats.ttest_ind(sample1, sample2, equal_var=False)

# # Print results
print("t-statistic:", t_stat)
print("p-value:", p_value)
# p-value  0.005


# Interpret results
alpha = 0.05
if p_value > alpha:
    print("Fail to reject the null hypothesis")
else:
    print("Reject the null hypothesis\n\n\n\n\n")

#No fim se observa que foi rejeitada a hipótese nula, sendo assim, apesar de próximo a idade das pessoas não são iguais como um todo, para as Raças/Cor Parda e Preta.
#Foi usado os vacinados do ano de 2022 em Recife para esta análise.







#2ª Análise
print("2ª Análise\n")
# Read data from CSV file
data = pd.read_csv('licitacoes_2022.csv', sep=',',
                   on_bad_lines='skip', low_memory=False)

data.dropna(subset=['VALORESTIMADO'], inplace=True)

#Levando como dica o que o professor falou em aula sobre as Licitações de Belo Jardim no ano de 2022, irei analizar e comparar os valores estimados de processos em andamento e deserto, 
#para saber qual a estimativa de gastos era maior.
#Tomando a hipótese Nula que os dois serão próximos o suficiente para serem considerados iguais.
sample1 = data[data['SITUACAOLICITACAO'] == 'Em Andamento']['VALORESTIMADO']
sample2 = data[data['SITUACAOLICITACAO'] == 'Processo Deserto']['VALORESTIMADO']

#Tratamento de erro humanos dos dados coletados
sample1 = pd.to_numeric(sample1, errors='coerce')
sample2 = pd.to_numeric(sample2, errors='coerce')

#cálculo da média para comparar com o T_Teste
mediaAndamento = sample1.mean()
mediaDeserto = sample2.mean()

# exibir o resultado
print(mediaAndamento)
print(mediaDeserto)

# # Perform t-test
t_stat, p_value = stats.ttest_ind(sample1, sample2, equal_var=False)

# # Print results
print("t-statistic:", t_stat)
print("p-value:", p_value)
# p-value  0.005


# Interpret results
alpha = 0.05
if p_value > alpha:
    print("Fail to reject the null hypothesis")
else:
    print("Reject the null hypothesis\n\n\n\n\n")

#Conseguimos no fim observar que também é rejeitado a hipótese nula, coisa que podemos observar desde suas médias, mas não teriamos como concluir sem o T_Teste.
#Concluimos então que as licitações desertas não gastam a mesma quantidade que as em andamento e que sua diferença é gritante.






#3ª Análise
print("3ª Análise\n")
# Read data from CSV file
data = pd.read_csv('licitacoes_2022.csv', sep=',',
                   on_bad_lines='skip', low_memory=False)

data.dropna(subset=['VALORESTIMADO'], inplace=True)

#Nesta análise irei comparar os dados das modalidades pregão eletrônico e Regime Diferenciado de Contratações (RDC) e 
#ver se seus valores estimados são suficientemente próximos para serem considerados o mesmo.
#Tomando como hipótese nula que os dois serão próximos o suficiente para serem considerados iguais.
sample1 = data[data['NOMEMODALIDADE'] == 'Pregão Eletrônico']['VALORESTIMADO']
sample2 = data[data['NOMEMODALIDADE'] == 'Regime Diferenciado de Contratações (RDC)']['VALORESTIMADO']

#Tratamento de erro humanos dos dados coletados
sample1 = pd.to_numeric(sample1, errors='coerce')
sample2 = pd.to_numeric(sample2, errors='coerce')

#cálculo da média para comparar com o T_Teste
mediaPregão = sample1.mean()
mediaRegime = sample2.mean()

# exibir o resultado
print(mediaPregão)
print(mediaRegime)

# # Perform t-test
t_stat, p_value = stats.ttest_ind(sample1, sample2, equal_var=False)

# # Print results
print("t-statistic:", t_stat)
print("p-value:", p_value)
# p-value  0.005


# Interpret results
alpha = 0.05
if p_value > alpha:
    print("Fail to reject the null hypothesis")
else:
    print("Reject the null hypothesis\n\n\n\n\n")

#Após análise observa-se que foi rejeitada a hipótese, considerando que muito provavelmente a modalidade Pregão Eletrônico é a mais comum, 
#portanto comparado os valores ficam diferentes demais, obseva-se isso pela sua média tambêm, mas diferentemente das duas análises anteriores, 
#o seu p_value nesta se aproximou bastante do nosso alpha, logo a diferença que é reefletida na média, não é tão gritante quanto na análise anterior, 
#onde a média refletiu a diferença dos dados.






#4ª Análise
print("4ª Análise\n")
# Read data from CSV file
data = pd.read_csv('licitacoes_2022.csv', sep=',',
                   on_bad_lines='skip', low_memory=False)

data.dropna(subset=['VALORESTIMADO'], inplace=True)

#Nesta análise vou observar os valores estimados em relação a objetos sondados.
#Tomando como Hipótese Nula que os dois objetos observados serão de valores tão próximos que podem ser considerados iguais.
sample1 = data[data['DESCRICAOOBJETO'] == 'EQUIPAMENTOS DE INFORMÁTICA']['VALORESTIMADO']
sample2 = data[data['DESCRICAOOBJETO'] == 'OBRAS']['VALORESTIMADO']

#Tratamento de erro humanos dos dados coletados
sample1 = pd.to_numeric(sample1, errors='coerce')
sample2 = pd.to_numeric(sample2, errors='coerce')

#cálculo da média para comparar com o T_Teste
mediaInfo = sample1.mean()
mediaObras = sample2.mean()

# exibir o resultado
print(mediaInfo)
print(mediaObras)

# # Perform t-test
t_stat, p_value = stats.ttest_ind(sample1, sample2, equal_var=False)

# # Print results
print("t-statistic:", t_stat)
print("p-value:", p_value)
# p-value  0.005


# Interpret results
alpha = 0.05
if p_value > alpha:
    print("Fail to reject the null hypothesis\n\n\n\n\n")
else:
    print("Reject the null hypothesis\n\n\n\n\n")

#Após análise feita, observamos que falhou ao rejeitar a hipótese com quase 92% de erro, logo podemos concluir que os gastos em relação a esses dois objetos é basicamente o mesmo, 
#tambêm é possivel observar que suas médias ficaram relativamente distantes, mas mesmo assim, foi aceita a hipótese nula, pois os dados são extremamente próximos.






#5ª Análise
print("5ª Análise\n")
# Read data from CSV file
data = pd.read_csv('vacinados-2022.csv', sep=';',
                   on_bad_lines='skip', low_memory=False)

data.dropna(subset=['idade'], inplace=True)

#Por fim nest análise, pensei em fazer um sample "duplo", então basicamente peguei os dados das pessoas Pretas dos Vacinados de Recife de 2022, e comparei a idade das pessoas de sexo feminino e masculino, no fim de tudo obtenho os dados de pessoas pretas do sexo masculino comparados com os dados de pessoas pretas do sexo feminino
#Tomamos nossa Hipótese nula na qual que por ambos tenham idades tão próximas que possam ser consideradas as mesmas. 
sample1 = data[data['sexo'] == 'FEMININO'][data['raca_cor'] == 'PRETA']['idade']
sample2 = data[data['sexo'] == 'MASCULINO'][data['raca_cor'] == 'PRETA']['idade']

#Tratamento de erro humanos dos dados coletados
sample1 = pd.to_numeric(sample1, errors='coerce')
sample2 = pd.to_numeric(sample2, errors='coerce')

#cálculo da média para comparar com o T_Teste
mediaMulherP = sample1.mean()
mediaHomemP = sample2.mean()

# exibir o resultado
print(mediaMulherP)
print(mediaHomemP)

# # Perform t-test
t_stat, p_value = stats.ttest_ind(sample1, sample2, equal_var=False)

# # Print results
print("t-statistic:", t_stat)
print("p-value:", p_value)
# p-value  0.005


# Interpret results
alpha = 0.05
if p_value > alpha:
    print("Fail to reject the null hypothesis")
else:
    print("Reject the null hypothesis\n\n\n\n\n")

#Observamos que  foi rejeitada a nossa hipótese nula, e que ouve um "erro" que na realidade é um aviso, 
#que basicamente diz que meus dados vão ser reindexados para os dois endereços, pegando um grupo menor de casos; 
#Voltando para a hipótese, podemos concluir que apesar de muito próximos as médias de idades, não podem ser consideradas as mesmas, 
#e vale observar que o nosso p_value confirma isso com praticamente 100% de precisão, pois o valor está multiplicado por 10 elevado a -86.