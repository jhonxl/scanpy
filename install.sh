#!/bin/bash

echo "[+] Verificando dependências..."

if ! command -v python3 &> /dev/null
then
    echo "[ERRO] Python3 não está instalado. Instale com: sudo apt install python3"
    exit 1
fi

echo "[OK] Python3 encontrado."

# (Opcional) criar ambiente virtual
echo "[+] Criando ambiente virtual (opcional)..."
python3 -m venv venv
source venv/bin/activate

echo "[+] Nenhuma dependência externa necessária para este projeto."
echo "[✔] Setup concluído. Rode com: python3 scanner.py"
