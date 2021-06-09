#Codigo feito baseado em outro codigo! assim voce tera um resultado mais rapido!
#AlisonProgramador
#12/maio!

try:
	import requests
	import json
	import os
	import sys
	from time import sleep as sl
except:
	print("\033[3;31m[??] Algo esta errado,percebemos que voce nao tem uma ferramenta instalada \npip install -r requirements.txt para instalar o quê falta!:(")
	print("Obrigado pela atenção")
else:

	while True:
		os.system("clear")
		print("""SEJA BEM VINDO,FAÇA UM BOM USO!
		\033[1;31m
################################
Facebook:
GitHub  :
[ 1 ] - Buscar repositirio
[ 2 ] - Suporte				
[ x ] - Sair""")
		try:
			escolhe = input("\033[1;31m[×]\033[35m O que você deseja: ")
		except KeyboardInterrupt:
			print("\033[1;31mSaindo...\033[m")
			sys.exit()
		else:
			print()
			if escolhe.isnumeric():
				escolhe = int(escolhe)
				if escolhe == 1:
					try:
						user = str(input("\033[1;31m[x]\033[m Usuario do github: "))
						ver_repost = str(input("\033[1;35m \033[35m Você deseja ver os repositórios? [Y/N]:>> ")).upper()
					except KeyboardInterrupt:
						print("\033[1;31mSaindo...\033[m")
						sys.exit()
					else:
						if ver_repost == "Y":
							url = "https://api.github.com/users/{}/repos".format(user)
							requisitar = requests.get(url)
							if requisitar.status_code == 200:
								print("\n\033[1;35m PROCESSANDO... {}\n".format(user))
								dados_api = json.loads(requisitar.text)
								for x in dados_api:
									resultado_api_repos = x
									for chave,valor in resultado_api_repos.items():
										if chave == "owner":
											pass
										else:
											if chave and valor:	
												if chave == "name":
													print("\033[1;31m[*] {}:\033[m {}".format(chave.replace(chave,"Repositório"),valor))
													print('\033[35m==============================')
												elif chave == "description":
													print("\033[1;31m[×] {}:\033[m {}".format(chave.replace(chave,"Descrição"),valor))
												elif chave == "forks":
													print("\033[1;31m[×] {}:\033[m {}".format(chave.replace(chave,"Forks"),valor))
												elif chave == "watchers":
													print("\033[1;31m {}:\033[m {}".format(chave.replace(chave,"Pessoas visualizando o repositório"),valor))
													print()
												elif chave == "clone_url":
													print("\033[1;31m[×] {}:\033[m {}".format(chave.replace(chave,"Link para clonar"),valor))
												elif chave == "language":
													print("\033[1;31m[×] {}:\033[m {}".format(chave.replace(chave,"PROGRAMADO EM>>"),valor))
												elif chave == "license":
													for ch,vl in valor.items():
														if ch == "name":
															print("\033[1;31m[×] {}:\033[m {}".format(ch.replace(ch,"Licença-codigo"),vl))
															break
													print()
								try:
									sair = str(input("\033[1;31m[×]\033[m S = sair / C = continuar [S/C]: ")).upper()
								except KeyboardInterrupt:
									print("\033[1;31mSaindo...\033[m")
									sys.exit()
								else:
									while sair not in "S"  and sair not in "C":
										try:
											sair = str(input("\033[1;31m[×]\033[m S = sair / C = continuar [S/C]: ")).upper()
										except KeyboardInterrupt:
											print("\033[1;31mSaindo...Volte sempre!\033[m")
											sys.exit()
										else:
											if sair == "S":
												sys.exit()
											elif sair == "C":
												pass
						elif ver_repost == "N":
							url = "https://api.github.com/users/{}".format(user)
							requisitar_url = requests.get(url)
							if requisitar_url.status_code == 200:
								dados = json.loads(requisitar_url.text)
								print()
								print("\033[1;35m[+]\033[m DADOS DA PÁGINA INICIAL:\n")
								for chave,valor in dados.items():
									if chave and valor:
										print("\033[1;31m[×] {}:\033[m {}".format(chave,valor))
								input("\n\033[1;31m[×]\033[mQUER VOLTAR AO MENU? APERTE ENTER ")
								os.system("clear")

				elif escolhe == 2:
					print('PROGRAMA CRIADO PARA ENCONTRAR PROJETOS NO GITHUB DE CRIADORES,MUITO UTIL E FACIL DE USAR ELE! CONTATO: {V1.9.0}')
					input("Aperte ENTER para voltar ao menu... ")
					os.system("clear")

			elif escolhe == "x" or escolhe == "x":
				sys.exit()
#AlisonProgramdor 
#codigo
#FIM DO CODIGO!
