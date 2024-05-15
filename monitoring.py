""" 
Traccia 3: Monitoraggio di Rete.

Realizzare uno script Python per monitorare lo stato di una rete, 
controllando la disponibilità di uno o più host tramite il protocollo ICMP (ping).
Lo script deve consentire all'utente di specificare gli indirizzi IP degli host da monitorare e deve visualizzare lo stato di ciascun host.
"""

from pythonping import ping
import ipaddress

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
        return response_list.success()  # True se l'host è raggiungibile, False altrimenti
    except TimeoutError:   
        print(f"Timeout scaduto durante il ping di {host}")
        return False  # Timeout scaduto durante il ping
    except Exception as e:
        print(f"Errore {e} durante il ping di {host}")
        return False  # Errore durante il ping

"""
    Funzione per verificare se un indirizzo IP è valido
    :param ip: Indirizzo IP da verificare
    :return: True se l'indirizzo IP è valido, False altrimenti
"""
def valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError as invalid_ip:
        print(f"{invalid_ip}")
        return False

"""
    Funzione principale per monitorare lo stato degli host
"""
def main():
    while True:
        try:        
            # Possibilità di inserire più host da monitorare
            num_hosts = int(input("\nInserire il numero di host da monitorare: "))
            if num_hosts < 1:
                raise ValueError("Numero di host da monitorare non valido: deve essere maggiore di 0")
            break 
        except ValueError as wrong_input:
            print(f"{wrong_input}, riprovare.")   

    hosts = []
    for i in range(num_hosts):
        while True: # Ciclo finché non viene inserito un indirizzo IP valido
            host = input(f"\nInserire l'indirizzo IP dell'host {i + 1}: ")
            if valid_ip(host):
                hosts.append(host)
                break
            else:
                print(f"Indirizzo IP {host} non valido, riprovare.")            

    print("\nStato degli host:")
    for host in hosts:
        if ping_host(host):
            print(f"{host} è online")
        else:
            print(f"{host} è offline")

if __name__ == "__main__":
    main()