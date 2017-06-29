# Git_Hook
Programma per il controllo dei commit git 
secondo le righe di commento nei sorgenti

# Installazione
Una volta aggiunta la cartella Git_Hook-master al vostro progetto entrate nella
cartella `Git_Hook-master\config_script` ed eseguite lo script `git_template_conf.cmd`
trammite doppio click (ATTENZIONE se è già presente uno script di pre-commit il nuovo codice verrà accodato a quello vecchio,
assicurarsi di eseguire lo script una sola volta in modo che non avvengano conflitti all'interno dello script)

Ora ogni volta che farete un commit tramite git su quel progetto tutti i 
sorgenti che che avete aggiunto verranno controllati

# Note
Non sarà più necessario eseguire nuovamente i passaggi descritti 
nell'installazione salvo nuovi aggiornamenti dello script `pre-commit`
contenuto in `Git_Hook-master\hooks`
