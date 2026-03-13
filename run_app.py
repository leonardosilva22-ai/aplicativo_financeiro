#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de inicialização para o Planejador Financeiro
Este arquivo é usado para criar um executável (.exe) do aplicativo
Inicia sem exibir terminal e abre automaticamente no navegador
Garante apenas uma instância em execução
"""

import subprocess
import sys
import os
import webbrowser
import time
import socket
from threading import Thread

def porta_em_uso(port=8501):
    """Verifica se a porta já está em uso"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex(('127.0.0.1', port))
        sock.close()
        return result == 0
    except:
        return False

def main():
    """Executa o aplicativo Streamlit em modo silencioso"""
    # Obter o diretório do script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Caminho do arquivo main.py
    main_file = os.path.join(script_dir, "main.py")
    
    # Verificar se o arquivo main.py existe
    if not os.path.exists(main_file):
        sys.exit(1)
    
    # Verificar se já existe Streamlit rodando
    if porta_em_uso(8501):
        # Se porta está em uso, apenas abre o navegador
        try:
            webbrowser.open("http://localhost:8501")
        except:
            pass
        return
    
    # Função para abrir o navegador em thread separada
    def open_browser():
        time.sleep(3)
        try:
            webbrowser.open("http://localhost:8501")
        except:
            pass
    
    # Iniciar thread para abrir navegador
    browser_thread = Thread(target=open_browser, daemon=True)
    browser_thread.start()
    
    # Redirecionar output para null device para não exibir console
    devnull = open(os.devnull, 'w')
    
    try:
        # Executar Streamlit em modo silencioso
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", main_file,
            "--logger.level=critical",
            "--client.showErrorDetails=false",
            "--browser.gatherUsageStats=false",
            "--server.port=8501",
            "--server.headless=true",
            "--client.toolbarMode=minimal"
        ], stdout=devnull, stderr=devnull)
    except Exception:
        pass
    finally:
        devnull.close()

if __name__ == "__main__":
    main()
