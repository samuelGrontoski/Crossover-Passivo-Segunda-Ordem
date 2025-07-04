# Projeto de Crossover Passivo de 2ª Ordem
Este repositório contém uma ferramenta computacional em Python para projetar, analisar e simular um crossover de áudio passivo de 2ª ordem com alinhamento Butterworth.

## Descrição
O programa calcula os valores de indutores (L) e capacitores (C) necessários para criar um filtro passa-baixas (LPF) para um woofer e um filtro passa-altas (HPF) para um tweeter, com base em uma frequência de corte e uma impedância de carga especificadas pelo usuário.

Além dos cálculos ideais, a ferramenta seleciona os componentes reais mais próximos de listas de valores comerciais e gera um gráfico de Bode comparativo, mostrando o impacto dessas escolhas do mundo real na resposta de frequência do sistema.

## Funcionalidades
- **Cálculo Automático:** Calcula os valores ideais de L e C para um filtro Butterworth de 2ª ordem.

- **Seleção de Componentes Reais:** Sugere os componentes comerciais mais próximos a partir de listas pré-definidas.

- **Simulação e Visualização:** Gera gráficos de Bode comparativos (Ideal vs. Real) para análise visual da performance do filtro.

- **Design Completo:** Projeta tanto o filtro Passa-Baixas (LPF) quanto o Passa-Altas (HPF).

- **Configurável:** Permite ao usuário alterar facilmente os parâmetros do projeto (frequência de corte e impedância) diretamente no código.

## Pré-requisitos
Para executar este script, você precisará ter o Python 3 instalado em seu sistema, juntamente com as seguintes bibliotecas:

- **NumPy:** Para cálculos numéricos eficientes.

- **Matplotlib:** Para a geração dos gráficos.

## Instalação
**1. Clone ou baixe o repositório:**
<br>
Salve o arquivo ```crossover_passivo.py``` (ou o nome que preferir) em seu computador.

**2. Instale as dependências:**
<br>
Abra um terminal ou prompt de comando e execute o seguinte comando para instalar as bibliotecas necessárias usando ```pip```:

```
pip install numpy matplotlib
```

## Como Executar
**1.** Navegue até o diretório onde você salvou o arquivo ```.py``` usando o terminal.
**2.** Execute o script com o seguinte comando:

```
python crossover_passivo.py
```

Ao executar, o programa irá:
<br>
**a.** Imprimir no console os valores ideais calculados e os valores dos componentes comerciais selecionados.
<br>
**b.** Abrir duas janelas de gráfico, uma para a resposta do LPF e outra para a resposta do HPF.

## Como Configurar para o Seu Projeto
Você pode  alterar os parâmetros do projeto para atender às suas necessidades. Abra o arquivo ```crossover_passivo.py``` em um editor de texto e modifique as seguintes linhas na função ```main()```:

```
def main():
    # Altere os valores abaixo para o seu projeto
    frequencia_corte = 2400.0  # Defina a frequência de corte em Hertz (ex: 3000.0)
    impedancia_carga = 4.0    # Defina a impedância dos alto-falantes em Ohms (ex: 8.0)

    # O restante do código usará estes parâmetros
    # ...
```

- ```frequencia_corte:``` Altere para a frequência de cruzamento desejada para seus alto-falantes.

- ```impedancia_carga:``` Altere para a impedância nominal do seu woofer e tweeter.

Se desejar, você também pode editar as listas ```CAPACITORES_COMERCIAIS_uF``` e ```INDUTORES_COMERCIAIS_mH``` para refletir os componentes que você tem disponíveis.
