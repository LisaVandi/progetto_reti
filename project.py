# Traccia 3: Monitoraggio di Rete

# da installare con pip install pythonping
from pythonping import ping 

"""
    Funzione per eseguire il comando ping e controllare lo stato di un host
    :param host: Indirizzo IP dell'host da monitorare
    :return: True se l'host è raggiungibile, False altrimenti
    Inoltre, gestisce anche eventuali eccezioni, come il timeout delle richieste ICMP.
"""
def ping_host(host):
    try:
        # Esegui un solo ping verso l'host con timeout di 2 secondi
        response_list = ping(host, count=1, timeout=2)
        # Controlla se il ping ha avuto successo: verifica se il valore medio del tempo di risposta (rtt_avg_ms) è diverso da None
        if response_list.rtt_avg_ms is not None:
            return True  # Host raggiungibile
        else:
            return False  # Host non raggiungibile
    except TimeoutError:    
        print(f"Timeout scaduto durante il ping di {host}")
        return False  # Timeout scaduto durante il ping
    except ConnectionError as e: # oppure Exception
        print(f"Errore {e} durante il ping di {host}")
        return False  # Errore durante il ping

"""
    Funzione principale per monitorare lo stato degli host
"""
def main():
    try:
        # Possibilità di inserire più host da monitorare
        num_hosts = int(input("Inserire il numero di host da monitorare: "))
        if num_hosts < 1:
            raise ValueError("Numero di host da monitorare non valido: deve essere maggiore di 0.")
        hosts = []
        for i in range(num_hosts):
            host = input(f"Inserisci l'indirizzo IP dell'host {i + 1}: ")
            hosts.append(host)

        print("\nStato degli host:")
        for host in hosts:
            if ping_host(host):
                print(f"{host} è online")
            else:
                print(f"{host} è offline")
    except ValueError as wrong_input:
        print(f"{wrong_input}")

if __name__ == "__main__":
    main()

# DA FARE: 
# verificare indirizzo ip valido
# capire perché non funziona online e offline
# relazione