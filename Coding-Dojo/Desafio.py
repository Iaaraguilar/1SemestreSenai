def explorar_planeta():
    iniciar = input('Deseja iniciar uma nova exploração? Sim (s) ou Não (Qualquer letra): ')
    
    if iniciar.lower() == 's':
        print('Exploração iniciada!')

        while True:
            obstaculo = input("Há alguma montanha no caminho? Sim (s) ou Não (Qualquer letra): ")

            if obstaculo.lower() == 's':
                continuar_escalando = True
                
                while continuar_escalando:
                    vai_escalar = input("A equipe irá tentar escalar a montanha (e) ou contornar (Qualquer letra): ")

                    if vai_escalar.lower() == 'e':
                        escalou = input("A equipe conseguiu escalar a montanha? Sim (s) ou Não (Qualquer letra): ")

                        if escalou.lower() == 's':
                            break
                        else:
                            continue
                    else:
                        break

            area_rica = input("A equipe encontrou uma área rica em minerais ou sinais de vida? Sim (s) ou Não (Qualquer letra): ")
            
            if area_rica.lower() == 's':
                print("Área explorada com sucesso! Dados foram coletados.")
                prosseguir = input("A equipe deseja prosseguir com a exploração? Sim (s) ou Não (Qualquer letra): ")

                if prosseguir.lower() == 's':
                    continue
                else:
                    print("Exploração concluída, a equipe retornou à nave!")
                    break
            else:
                continue
    else:
        print("Exploração não iniciada!")

# Executa a função
explorar_planeta()
