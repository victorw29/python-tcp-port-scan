#Projeto: Port Scanner TCP Assíncrono
#Objetivo:
#- Estudar o funcionamento do protocolo TCP
#- Compreender o conceito de portas e serviços
#- Explorar concorrência com asyncio
#- Introduzir noções básicas de cibersegurança

#Tipo de scan:
#- TCP Connect Scan (3-way handshake completo)

#Observação:
#- Projeto educacional
#- Não utilizar em redes sem autorização

#Importando bibliotecas
import asyncio 

#Criação da classe 
class Scanner:
    def __init__(self, ip_alvo, limite_conexoes):
        self.ip_alvo = ip_alvo  #atributo para recebimento do alvo
        #Semáforo limita o número de conexões simultâneas
        #Evita sobrecarregar o sistema e reduz chances de bloqueio por firewall
        self.semaforo = asyncio.Semaphore(limite_conexoes) 
        self.portas_abertas = []

    #definição do primeiro método/função para testar uma porta
    async def port_scan(self, porta):
        #Cada porta é testada dentro de um contexto assíncrono
        #O semáforo garante que apenas o numero sugerido pelo usuário de conexões ocorram ao mesmo tempo
        async with self.semaforo:
            print(f"testando portas {porta}")
            try: 
                leitor, escritor = await asyncio.wait_for(
                    asyncio.open_connection(self.ip_alvo, porta),
                    timeout = 1.0 #tempo máximo de espera pela resposta
                ) 

                #Se chegou aqui, a porta está aberta
                self.portas_abertas.append(porta)
                
                #Encerra a conexão corretamente (envia FIN)
                escritor.close()
                await escritor.wait_closed()
            


            except ConnectionRefusedError:
                print(f"[X] Porta {porta}: FECHADA")

            except asyncio.TimeoutError:
                print(f"[!] Porta {porta}: SEM RESPOSTA (FILTRADA ou TIMEOUT)")

            except Exception:
                print(f"[?] Porta {porta}: ERRO DESCONHECIDO")

    #criação de corrotina por porta
    async def iniciar_scan(self, inicio, fim):
        tarefas = [self.port_scan(p) for p in range(inicio, fim + 1)]
        await asyncio.gather(*tarefas)

        
        #Após o término do scan, as portas abertas são exibidas em ordem crescente
        #A ordenação melhora a legibilidade dos resultados
        print("\n Scan Finalizado!")
        for porta in sorted(self.portas_abertas):
            print(f"[✔] porta: {porta}: ABERTA") 

#Função principal
async def main():
    scanner = Scanner("", 100) #definição de alvo e limite de conexões
    await scanner.iniciar_scan(8000, 8100) #definição de intervalo das portas
    
if __name__ == "__main__":
    asyncio.run(main())
        
