import numpy as np
import matplotlib.pyplot as plt
import math

# Tabelas de Valores Comerciais Padrão
CAPACITORES_COMERCIAIS_uF = [
    1.0, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2, 10,
    12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82, 100
]

INDUTORES_COMERCIAIS_mH = [
    0.10, 0.12, 0.15, 0.18, 0.22, 0.27, 0.33, 0.39, 0.47, 0.56, 0.68,
    0.82, 1.0, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2,
    10, 12, 15
]

def calcular_componentes_ideais(fc, R):
    L_ideal = (R * math.sqrt(2)) / (2 * math.pi * fc)
    C_ideal = 1 / (2 * math.pi * fc * R * math.sqrt(2))
    return L_ideal, C_ideal

def encontrar_mais_proximo(valor_ideal, lista_comercial):
    return min(lista_comercial, key=lambda x: abs(x - valor_ideal))

def plotar_grafico_bode(fc, R, L_ideal, C_ideal, L_real, C_real, tipo_filtro='LPF'):
    freq = np.logspace(1, 5, 500) # De 10 Hz a 100 kHz
    omega = 2 * np.pi * freq

    # Resposta Ideal de Butterworth
    if tipo_filtro == 'LPF':
        mag_ideal = 20 * np.log10(1 / np.sqrt(1 + (freq / fc)**4))
        # Função de Transferência Real (LPF: 1 / (s^2*LC + s*L/R + 1))
        H_real = 1 / (1 - omega**2 * L_real * C_real + 1j * omega * L_real / R)
        titulo = 'Filtro Passa-Baixas (LPF) - Woofer'
    elif tipo_filtro == 'HPF':
        mag_ideal = 20 * np.log10(1 / np.sqrt(1 + (fc / freq)**4))
        # Função de Transferência Real (HPF: s^2 / (s^2 + s/(RC) + 1/(LC)))
        H_real = (-omega**2) / (1/(L_real*C_real) - omega**2 + 1j * omega / (R * C_real))
        titulo = 'Filtro Passa-Altas (HPF) - Tweeter'
    else:
        return

    mag_real = 20 * np.log10(np.abs(H_real))

    # Plotagem
    plt.figure(figsize=(10, 6))
    plt.semilogx(freq, mag_ideal, 'b--', label=f'Ideal (fc={fc} Hz)')
    plt.semilogx(freq, mag_real, 'r-', label='Real (Componentes Comerciais)')
    plt.axvline(x=fc, color='gray', linestyle=':', label=f'fc nominal ({fc} Hz)')
    
    # Calcula e marca a nova fc real
    fc_real_idx = np.argmin(np.abs(mag_real - (-3)))
    fc_real = freq[fc_real_idx]
    plt.axvline(x=fc_real, color='red', linestyle=':', label=f'fc real (~{int(fc_real)} Hz)')
    
    plt.title(f'Gráfico de Bode Comparativo: {titulo}')
    plt.xlabel('Frequência (Hz)')
    plt.ylabel('Magnitude (dB)')
    plt.grid(True, which="both", ls="-", alpha=0.5)
    plt.xlim(100, 20000)
    plt.ylim(-40, 5)
    plt.legend()
    plt.show()

def main():
    # Parâmetros do Projeto
    frequencia_corte = 2400.0  # Hz
    impedancia_carga = 4.0    # Ohms

    print("--- Projeto de Crossover Passivo de 2ª Ordem para Sistemas de Áudio ---")
    print(f"Parâmetros: Frequência de Corte = {frequencia_corte} Hz, Impedância = {impedancia_carga} Ohms\n")

    # Calcular os valores ideais
    L_ideal_H, C_ideal_F = calcular_componentes_ideais(frequencia_corte, impedancia_carga)
    L_ideal_mH = L_ideal_H * 1000
    C_ideal_uF = C_ideal_F * 1e6

    print("--- Valores Ideais Calculados ---")
    print(f"Indutor Ideal (L): {L_ideal_mH:.3f} mH")
    print(f"Capacitor Ideal (C): {C_ideal_uF:.3f} μF\n")

    # Sugerir componentes reais
    L_real_mH = encontrar_mais_proximo(L_ideal_mH, INDUTORES_COMERCIAIS_mH)
    C_real_uF = encontrar_mais_proximo(C_ideal_uF, CAPACITORES_COMERCIAIS_uF)
    L_real_H = L_real_mH / 1000
    C_real_F = C_real_uF / 1e6
    
    print("--- Componentes Comerciais Mais Próximos Selecionados ---")
    print(f"Indutor Real (L): {L_real_mH} mH")
    print(f"Capacitor Real (C): {C_real_uF} μF\n")

    # Gerar Gráfico de Bode comparativo
    print("Gerando gráficos de Bode...")
    
    # Filtro Passa-Baixas (LPF)
    plotar_grafico_bode(frequencia_corte, impedancia_carga, L_ideal_H, C_ideal_F, L_real_H, C_real_F, 'LPF')
    
    # Filtro Passa-Altas (HPF)
    plotar_grafico_bode(frequencia_corte, impedancia_carga, L_ideal_H, C_ideal_F, L_real_H, C_real_F, 'HPF')

    print("Análise concluída.")

if __name__ == '__main__':
    main()