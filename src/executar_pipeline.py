import os
import glob
import papermill as pm
import pandas as pd
import matplotlib.pyplot as plt

def rodar_pipeline_completa():
    # Parâmetros para o ataque de força bruta
    k_valores = [2, 3, 5, 10, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500]
    l_valores = [1, 2, 3, 4, 5]
    t_valores = [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50]

    notebook_input = "notebooks/poc1.ipynb"
    os.makedirs("outputs", exist_ok=True)

    total_execucoes = len(k_valores) * len(l_valores) * len(t_valores)
    print("====== INICIANDO PIPELINE DE FORÇA BRUTA ======")
    print(f"Total de combinações a executar: {total_execucoes}")

    # Loops aninhados corrigidos
    for k in k_valores:
        for l in l_valores:
            for t in t_valores:
                notebook_output = f"outputs/exec_k{k}_l{l}_t{t}.ipynb"
                print(f"-> Executando iteração com K={k}, L={l}, T={t}...")

                try:
                    # Injetando as variáveis corretas do seu notebook
                    pm.execute_notebook(
                        notebook_input,
                        notebook_output,
                        parameters=dict(
                            k_alvo=k, l_alvo=l, t_alvo=t,
                            usar_k=True, usar_l=True, usar_t=True
                        )
                    )
                except Exception as e:
                    print(f"[ERRO] Falha crítica na execução de K={k}, L={l}, T={t}: {e}")
                    continue

    print("\n====== CONSOLIDANDO RESULTADOS ======")
    arquivos_parciais = glob.glob("outputs/parcial_*.csv")

    if not arquivos_parciais:
        print("[ERRO] Nenhum arquivo parcial de métricas foi gerado.")
        return
    
    lista_dfs = [pd.read_csv(fp) for fp in arquivos_parciais]
    df_consolidado = pd.concat(lista_dfs, ignore_index=True)
    
    # Ordena os dados para a tabela ficar estruturada de forma lógica
    df_consolidado = df_consolidado.sort_values(by=['k_alvo', 'l_alvo', 't_alvo']).reset_index(drop=True)

    caminho_tabela = "outputs/resultado_final.csv"
    df_consolidado.to_csv(caminho_tabela, index=False)

    print("\n--- TABELA DE MÉTRICAS CONSOLIDADAS ---")
    print(df_consolidado.to_markdown(index=False))

    # Geração do Gráfico: Trade-off de Privacidade vs Perda de Dados
    plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
    fig, ax1 = plt.subplots(figsize=(10, 6))
    
    # Plotamos a % de registros suprimidos vs Acurácia
    scatter = ax1.scatter(
        df_consolidado['registros_suprimidos_porcentagem'], 
        df_consolidado['acuracia_com_privacidade'],
        c=df_consolidado['k_alvo'], cmap='viridis', alpha=0.7, edgecolors='k', s=50
    )
    
    baseline = df_consolidado['acuracia_sem_privacidade'].iloc[0]
    ax1.axhline(y=baseline, color='red', linestyle='--', label=f'Baseline sem anonimização ({baseline:.2f}%)')

    ax1.set_xlabel('% de Registros Suprimidos (Perda de Informação)')
    ax1.set_ylabel('Acurácia do Modelo Random Forest (%)')
    plt.title('Trade-off: Rigidez da Anonimização vs Performance da IA', fontsize=14, pad=15)
    
    # Adiciona uma barra de cor para sabermos qual ponto representa qual valor de K
    cbar = plt.colorbar(scatter)
    cbar.set_label('Valor do K-Anonimato')
    
    ax1.legend()
    fig.tight_layout()

    caminho_grafico = "outputs/grafico_tradeoff_privacidade.png"
    plt.savefig(caminho_grafico, dpi=300)
    print(f"\n[SUCESSO] Gráfico analítico gerado e salvo em: {caminho_grafico}")

if __name__ == "__main__":
    rodar_pipeline_completa()