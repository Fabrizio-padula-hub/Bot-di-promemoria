# Bot di Promemoria

Un bot Telegram che permette agli utenti di impostare promemoria personalizzati con un comando semplice. Il bot invia notifiche quando il promemoria è pronto.

## Introduzione

Questo è un semplice bot per Telegram che consente agli utenti di impostare promemoria con un formato di tempo facile da usare (es. `5m`, `2h`, `1d`). Una volta che il tempo specificato è trascorso, il bot invia una notifica di promemoria all'utente.

--- 

## Requisiti

- **Python 3.8** o superiore.

---

## Come creare un nuovo bot e recuperare il token su Telegram

1. **Cerca BotFather**: Vai su Telegram e cerca il bot chiamato **BotFather**.
2. **Crea un nuovo bot**: Avvia una chat con BotFather e invia il comando `/newbot`.
3. **Scegli un nome per il bot**: Quando BotFather ti chiederà, scegli un nome per il tuo bot. Questo sarà il nome che vedranno gli utenti.
4. **Scegli un username per il bot**: Poi, scegli un **username** per il bot. Deve essere unico e finire con `bot` (esempio: `reminder_bot`).
5. **Ricevi il token**: Dopo aver creato il bot, BotFather ti invierà un **token** che dovrai utilizzare per autenticare il tuo bot. Questo token ha un formato simile a questo:123456789:ABCDEFghijkLMNOPQRSTUVWXYZ12345678
6. **Conserva il token**: Copia questo token, ti servirà per configurare il bot nel tuo progetto.

---

## Dipendenze

Il progetto richiede la libreria `python-telegram-bot` per interagire con l'API di Telegram. Per installarla, esegui il seguente comando:

```bash
pip install python-telegram-bot
```
---

## Configurazione

1. **Rinomina il file `config.example.py`**: Dopo aver scaricato il progetto, rinomina il file `config.example.py` in `config.py`. Questo file contiene il modello di configurazione per il bot.

2. **Aggiungi il tuo token**: Apri il file `config.py` e incolla il **token** del tuo bot al posto del segnaposto `Il_tuo_token_qui`:

   ```python
   # config.py
   TOKEN = 'Il_tuo_token_qui'

---

## Esegui il Bot

1. **Avvia il bot**: Una volta configurato il file `config.py` con il tuo token, esegui il bot con il seguente comando:

   ```bash
   python bot.py
   ```

---

### **Comandi disponibili**:
```markdown
## Comandi

Ecco i comandi principali che puoi usare con il bot:

- **/start**: Avvia la conversazione con il bot e ricevi una breve descrizione su come utilizzarlo.
- **/remind <tempo> <messaggio>**: Imposta un promemoria. Esempio: `/remind 10m Compra il latte`. Il bot invierà una notifica al termine del tempo impostato.

---

Con queste informazioni puoi creare il bot e iniziare a usarlo nel progetto.

---