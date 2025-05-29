# 🔍 Port Scanner TCP (Python)

Este é um scanner de portas TCP simples feito em Python. Ele permite verificar quais portas estão abertas em um ou mais hosts.

## 🚀 Funcionalidades

- Scaneia múltiplos IPs ou domínios
- Detecta se a porta está aberta ou fechada
- Timeout configurável
- Lista de portas personalizável

## 🧠 Uso educativo

> ⚠️ **Este projeto é apenas para fins educacionais e testes em ambientes controlados.**
> **Não escaneie redes de terceiros sem autorização explícita.**

---

## 📦 Requisitos

- Python 3.x
- Não é necessário instalar bibliotecas externas

---

## ▶️ Como usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/jhonxl/scanpy
   cd scanpy
   ```

2. Execute o script:
   ```bash
   python3 scanner.py
   ```

3. Digite os IPs separados por vírgula:
   ```
   Digite os hosts (ex: 192.168.0.1, 192.168.0.2): 
   ```

---

## 🖥️ Exemplo de saída

```text
[+] Iniciando scan em: 192.168.0.1
[ABERTA] Porta 80 está aberta.
[FECHADA] Porta 22 está fechada.

[+] Iniciando scan em: 192.168.0.2
[FECHADA] Porta 80 está fechada.
```

---

## 📄 Licença

Este projeto está licenciado sob a Licença MIT.
