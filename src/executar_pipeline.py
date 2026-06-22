import os
import glob
import papermill as pm
import pandas as pd

def rodar_pipeline_completa():
    # Parâmetros
    k_valores = [2, 3, 5, 10, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500]
    l_valores = [2, 3, 4, 5, 6, 7, 8, 9]
    t_valores = [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50]

    diretorio_script = os.path.dirname(os.path.abspath(__file__))
    notebook_input = os.path.join(diretorio_script, "poc1.ipynb")
    pasta_outputs = os.path.join(diretorio_script, "outputs")
    os.makedirs(pasta_outputs, exist_ok=True)

    tarefas = []

    # 1. Somente K (Executa 15 vezes)
    for k in k_valores:
        tarefas.append({'k': k, 'l': l_valores[0], 't': t_valores[0], 'uk': True, 'ul': False, 'ut': False})

    # 2. Somente K e L (Executa 75 vezes)
    for k in k_valores:
        for l in l_valores:
            tarefas.append({'k': k, 'l': l, 't': t_valores[0], 'uk': True, 'ul': True, 'ut': False})

    # 3. Somente K e T (Executa 150 vezes)
    for k in k_valores:
        for t in t_valores:
            tarefas.append({'k': k, 'l': l_valores[0], 't': t, 'uk': True, 'ul': False, 'ut': True})

    # 4. K, L e T juntos (Executa 750 vezes)
    for k in k_valores:
        for l in l_valores:
            for t in t_valores:
                tarefas.append({'k': k, 'l': l, 't': t, 'uk': True, 'ul': True, 'ut': True})

    print("====== INICIANDO PIPELINE DE FORÇA BRUTA ======")
    print(f"Total de combinações únicas a executar: {len(tarefas)}")

    for i, t in enumerate(tarefas, 1):
        notebook_output = os.path.join(pasta_outputs, f"exec_{i}.ipynb")
        print(f"-> [{i}/{len(tarefas)}] Iteração: K={t['k']} L={t['l']} T={t['t']} | Flags(K:{t['uk']} L:{t['ul']} T:{t['ut']})")

        try:
            pm.execute_notebook(
                notebook_input,
                notebook_output,
                parameters=dict(
                    k_alvo=t['k'], l_alvo=t['l'], t_alvo=t['t'],
                    usar_k=t['uk'], usar_l=t['ul'], usar_t=t['ut']
                )
            )
        except Exception as e:
            print(f"[ERRO] Falha crítica na iteração {i}: {e}")
            continue

    print("\n====== CONSOLIDANDO RESULTADOS ======")
    arquivos_parciais = glob.glob(os.path.join(pasta_outputs, "parcial_*.csv"))

    if not arquivos_parciais:
        print("[ERRO] Nenhum arquivo parcial de métricas foi gerado.")
        return
    
    lista_dfs = [pd.read_csv(fp) for fp in arquivos_parciais]
    df_consolidado = pd.concat(lista_dfs, ignore_index=True)
    
    # Ordenação lógica para a tabela CSV
    df_consolidado = df_consolidado.sort_values(by=['cenario', 'k_alvo', 'l_alvo', 't_alvo']).reset_index(drop=True)

    caminho_tabela = os.path.join(pasta_outputs, "resultado_final.csv")
    df_consolidado.to_csv(caminho_tabela, index=False)
    
    print("\n[SUCESSO] Tabela salva com os múltiplos cenários.")

if __name__ == "__main__":
    rodar_pipeline_completa()