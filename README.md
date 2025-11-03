# 🩺 Doctor-AI (n8n Workflow)

**Doctor-AI** è un workflow per n8n che utilizza **Google Gemini** come modello di intelligenza artificiale per analizzare sintomi descritti in linguaggio naturale e restituire un output strutturato con possibili condizioni diagnostiche e note esplicative.  

⚠️ **Avvertenza**: Questo workflow è a scopo **dimostrativo ed educativo**.  
Non sostituisce il parere di un medico o di un professionista sanitario qualificato.

---

## 📂 Struttura del progetto
```
doctor-AI.json       # il workflow principale
.gitignore           # evita di committare file sensibili
README.md            # documentazione del progetto
```

---

## ⚙️ Come funziona il workflow

1. **Trigger chat** → riceve il messaggio dell’utente con i sintomi.  
2. **AI Agent (Gemini)** → interpreta il testo e formula possibili diagnosi.  
3. **Memoria breve** → conserva il contesto delle ultime interazioni.  
4. **Structured Output Parser** → forza l’output in formato JSON con questa struttura:  
   ```json
   {
     "conditions": [
       {
         "name": "Nome condizione",
         "icd10": "Codice ICD-10",
         "probability_percent": 0,
         "rationale": "Spiegazione"
       }
     ],
     "notes": "Considerazioni aggiuntive"
   }
   ```

---

## 💡 Esempio di utilizzo

### Input (utente):
> “Ho febbre a 38°, mal di gola e tosse secca da due giorni. Tampone COVID negativo.”

### Output (esempio generato):
```json
{
  "conditions": [
    {
      "name": "Faringite virale",
      "icd10": "J02.9",
      "probability_percent": 45,
      "rationale": "Sintomi acuti, febbre moderata, tampone COVID negativo."
    },
    {
      "name": "Influenza",
      "icd10": "J11.1",
      "probability_percent": 35,
      "rationale": "Febbre, tosse, stanchezza; tipico quadro influenzale."
    },
    {
      "name": "COVID-19",
      "icd10": "U07.1",
      "probability_percent": 10,
      "rationale": "Sintomi compatibili ma tampone rapido negativo."
    }
  ],
  "notes": "Output generato automaticamente, non sostituisce consulto medico."
}
```

---

## 🚀 Come usare il workflow

1. **Clona questa repository**
   ```bash
   git clone https://github.com/<tuo-username>/doctor-ai.git
   cd doctor-ai
   ```

2. **Apri n8n**  
   Puoi usare n8n Desktop, n8n Cloud o un’istanza in Docker.

3. **Importa il workflow**
   - Vai su n8n → **Workflows** → **Import from File**
   - Seleziona `workflows/doctor-AI.json`

4. **Configura la chiave API Gemini**
   - Copia `.env.example` in `.env`:
     ```bash
     cp .env.example .env
     ```
   - Inserisci la tua chiave reale in `GEMINI_API_KEY`
   - Nel workflow le chiamate usano `{{$env.GEMINI_API_KEY}}`

---

## 📜 Licenza
MIT – puoi usare, modificare e migliorare liberamente questo workflow.
