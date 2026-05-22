# Gerador-de-Senhas

Script feito em Python usando a biblioteca secrets

## Diferença de Uso: Secrets x Random

Duas bibliotecas utilizadas muito para criar um gerador de senhas, mas com grandes diferenças 

  Random
Usa um algoritmo matemático (Mersenne Twister) baseado em um "seed" (semente).

### Por que não é recomendado?
Se um hacker descobrir o estado interno do gerador, ele preverá todas as próximas senhas.

  Secrets
  Gera números baseados em fontes aleatórias do sistema operacional.

  ### Diferencial

  Totalmente imprevisível. Um hacker não consegue adivinhar a próxima senha.
