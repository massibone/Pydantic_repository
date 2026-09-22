# Pydantic_repository

📂 Progetto: Pydantic Repository
E' tutto organizzato tutto in modo ordinato per gestire sia le interfacce web che l'intelligenza artificiale, mantenendo i dati sempre sincronizzati.

🏗️ Com'è strutturato il progetto?
Abbiamo diviso le responsabilità in due cartelle principali, così da non fare mai confusione:

fast-api/ 🌐: Qui trovi tutto quello che serve per la gestione delle interfacce web e delle API. È il motore che permette di comunicare con gli strumenti che utilizzi quotidianamente (come SIGEDO o i servizi di protocollazione).

llm-agent/ 🤖: Qui vive la "mente" del progetto. È la parte dedicata all'agente basato su intelligenza artificiale, pronto a elaborare dati e supportarti nelle procedure più complesse.

common/ 💎: La nostra zona speciale. Qui teniamo i modelli Pydantic condivisi. Qualsiasi modifica fatta qui viene applicata automaticamente sia alle API che all'Agente, garantendo che i dati siano sempre coerenti.

🚀 Come iniziare
Per far partire il tutto, ti basterà seguire questi semplici passaggi:

Attiva l'ambiente: Assicurati di essere dentro il tuo ambiente virtuale.

Lancia la parte che ti serve:

Vuoi avviare il server web? Entra nella cartella e avvia FastAPI.

Vuoi testare l'agente? Spostati nella cartella llm-agent e avvialo.

Sicurezza: Grazie a Pydantic, i dati che passano tra l'API e l'Agente sono sempre controllati e validati.


