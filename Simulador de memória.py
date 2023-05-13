opção=''
endereço=""
célula1="00000000"
célula2="00000000"
célula3="00000000"
célula4="00000000"
célula5="00000000"
célula6="00000000"
célula7="00000000"
célula8="00000000"
célula9="00000000"
célula10="00000000"
célula11="00000000"
célula12="00000000"
célula13="00000000"
célula14="00000000"
célula15="00000000"
célula16="00000000"
while True:
 
 opção= input('Digite W para escrever, R para ler, L para listar toda a memória e qualquer tecla para parar: ')
 if (opção!="W") and (opção!="R") and (opção!="L"):
  break


 if opção == "L":
  print(f'''Todos os estados:
  {célula1}
  {célula2}
  {célula3}
  {célula4}
  {célula5}
  {célula6}
  {célula7}
  {célula8}
  {célula9}
  {célula10}
  {célula11}
  {célula12}
  {célula13}
  {célula14}
  {célula15}
  {célula16}
  ''')
 
 
 elif opção == "W":
  endereço=input("Digite o endereço de 4 bits: ")
  if endereço == "0000":
   célula1=input('Digite o dado de 8 bits:')
  if endereço == "0001":
   célula2=input('Digite o dado de 8 bits:')
  if endereço == "0010":
   célula3=input('Digite o dado de 8 bits:')
  if endereço == "0011":
   célula4=input('Digite o dado de 8 bits:')
  if endereço == "0100":
   célula5=input('Digite o dado de 8 bits:')
  if endereço == "0101":
   célula6=input('Digite o dado de 8 bits:')
  if endereço == "0110":
   célula7=input('Digite o dado de 8 bits:')
  if endereço == "0111":
   célula8=input('Digite o dado de 8 bits:')
  if endereço == "1000":
   célula9=input('Digite o dado de 8 bits:')
  if endereço == "1001":
   célula10=input('Digite o dado de 8 bits:')
  if endereço == "1010":
   célula11=input('Digite o dado de 8 bits:')
  if endereço == "1011":
   célula12=input('Digite o dado de 8 bits:')
  if endereço == "1100":
   célula13=input('Digite o dado de 8 bits:')
  if endereço == "1101":
   célula14=input('Digite o dado de 8 bits:')
  if endereço == "1110":
   célula15=input('Digite o dado de 8 bits:')
  if endereço == "1111":
   célula16=input('Digite o dado de 8 bits:')


 elif opção == 'R':
  endereço=input("Digite o endereço de 4 bits: ")
  if endereço == "0000":
   print(célula1)
  if endereço == "0001":
   print(célula2)
  if endereço == "0010":
   print(célula3)
  if endereço == "0011":
   print(célula4)
  if endereço == "0100":
   print(célula5)
  if endereço == "0101":
   print(célula6)
  if endereço == "0110":
   print(célula7)
  if endereço == "0111":
   print(célula8)
  if endereço == "1000":
   print(célula9)
  if endereço == "1001":
   print(célula10)
  if endereço == "1010":
   print(célula11)
  if endereço == "1011":
   print(célula12)
  if endereço == "1100":
   print(célula13)
  if endereço == "1101":
   print(célula14)
  if endereço == "1110":
   print(célula15)
  if endereço == "1111":
   print(célula16)
print('Fim da execução do programa, obrigado por testar')