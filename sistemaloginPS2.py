#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#~criar um sistema para cadastrar os dados e uma senha~ *jogar num banco de dados*
#criar um sistema de login em que o nome de usuario seja o nome e a senha seja a que foi cadastrada
#ao logar, os dados do usuario serão mostrados
#ATENÇÃO, O ERRO É QUE O LINK DAS IMAGENS SÃO DIFERENTES PRA CADA CHAR


# In[61]:


dados=[]
personagens=['Anji','Axl','Chipp','Faust','Giovanna','Goldlewis','I-no','Jack-o','Ky','Leo',
             'May','Millia','Nagoriyuki','Potemkin','Ramlethal','Sol','Zato-1']



usuario=str(input('Crie o seu login:  '))

senha=' '
senhaverificar=''
while senhaverificar != senha:
    senha=str(input('Crie uma senha:  '))
    senhaverificar=str(input('Repita sua senha.'))
    if senhaverificar != senha:
        print('Senhas não conhecidem, favor digitar novamente sua senha.')
#até aqui ok//

nome=str(input('Digite seu nome:  '))       
idade=str(int(input('Digite sua idade: ')))


char=' '
while char not in personagens:
    char=str(input('Personagem utilizado: ').capitalize())
    if char not in personagens:
        print('Personagem não existe, por favor tente novamente.')
    




#cadastras esses dados num banco de dados
dados.append([usuario,senha,nome,idade,char])
bancodedados=open(f'{usuario}_{senha}.txt', 'w')
bancodedados.write(f"Parabéns, {nome}!\n")
bancodedados.write(f"Cadastro já realizado, o torneio será realizado dia 30/02/2022\n")
bancodedados.write(f"O personagem escolhido foi {char}!\n")
bancodedados.write(f"Boa sorte!\n")
bancodedados.close()
print('=-'*30,'=')
print('CADASTRO FINALIZADO.')
print('O torneio será realizado no dia 30/02/2022')
print('Para acessar as informações do seu cadastro, por favor insira seu login e senha.')
print('=-'*30,'=')





# In[62]:


#apos cadastrado, fazer o login

usuariologin=input('Digite seu usario: ')
senhalogin=input('Digite sua senha:  ')

arqv=open(f'{usuariologin}_{senhalogin}.txt')




print('=-'*30,'=')
print(arqv.read())
print('=-'*30,'=')









    

